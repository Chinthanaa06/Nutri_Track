from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.db.database import Base, engine, get_db
from app.models.entities import Child, User, Visit
from app.schemas.records import ChildInput, LoginInput, VisitInput
from app.services.growth import calculate_z_scores
from app.services.classification import classify_status, recommendations
from app.services.risk import early_risk_score, explain_factors

Base.metadata.create_all(bind=engine)
app = FastAPI(title="NutriTrack API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
def seed_demo_user():
    db = next(get_db())
    try:
        if not db.query(User).filter_by(username="demo").first():
            db.add(User(username="demo", password="nutri-demo"))
            db.commit()
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok", "service": "nutritrack-api"}

@app.post("/login")
def login(payload: LoginInput, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=payload.username, password=payload.password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid demo username or password")
    return {"message": "Login successful", "username": user.username}

@app.post("/children")
def create_child(payload: ChildInput, db: Session = Depends(get_db)):
    if payload.sex.upper() not in {"M", "F"}:
        raise HTTPException(status_code=422, detail="sex must be M or F")
    if db.query(Child).filter_by(child_code=payload.child_code).first():
        raise HTTPException(status_code=409, detail="Child code already exists")
    child_data = payload.model_dump()
    child_data["sex"] = payload.sex.upper()
    child = Child(**child_data)
    db.add(child); db.commit(); db.refresh(child)
    return {"id": child.id, "child_code": child.child_code, "name": child.name}

@app.post("/visits")
def add_visit(payload: VisitInput, db: Session = Depends(get_db)):
    child = db.query(Child).filter_by(id=payload.child_id).first()
    if not child:
        raise HTTPException(status_code=404, detail="Child not found")
    values = payload.model_dump()
    scores = calculate_z_scores(values["age_months"], child.sex, values["weight_kg"], values["height_cm"])
    status = classify_status(scores["waz"], scores["haz"], scores["whz"], values["muac_cm"])
    history = [{"age_months": v.age_months, "whz": v.whz, "muac_cm": v.muac_cm,
                "weight_kg": v.weight_kg, "recent_illness": v.recent_illness} for v in child.visits]
    current = {**values, **scores}
    risk = early_risk_score(history + [current])
    visit = Visit(**values, **scores, status=status, risk_score=risk, recorded_at=datetime.utcnow())
    db.add(visit); db.commit(); db.refresh(visit)
    return {"visit_id": visit.id, **scores, "status": status, "risk_score": risk,
            "risk_label": "High" if risk >= .65 else "Moderate" if risk >= .4 else "Low",
            "factors": explain_factors({**values, **scores}),
            "recommendations": recommendations(status),
            "disclaimer": "Screening aid only, not a medical diagnosis."}

@app.get("/children")
def list_children(db: Session = Depends(get_db)):
    children = db.query(Child).all()
    return [{"id": c.id, "child_code": c.child_code, "name": c.name,
             "age_months": c.age_months, "sex": c.sex} for c in children]

@app.get("/children/{child_id}/visits")
def child_visits(child_id: int, db: Session = Depends(get_db)):
    child = db.query(Child).filter_by(id=child_id).first()
    if not child: raise HTTPException(status_code=404, detail="Child not found")
    return [{"id": v.id, "age_months": v.age_months, "weight_kg": v.weight_kg,
             "status": v.status, "risk_score": v.risk_score, "waz": v.waz,
             "haz": v.haz, "whz": v.whz} for v in child.visits]

@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    visits = db.query(Visit).all()
    children = db.query(Child).all()
    distribution = {}
    for visit in visits: distribution[visit.status] = distribution.get(visit.status, 0) + 1
    high = [{"child": v.child.name, "status": v.status, "risk_score": v.risk_score}
            for v in visits if v.risk_score >= .65]
    return {"children_count": len(children), "visits_count": len(visits),
            "risk_distribution": distribution, "high_risk": high}

@app.get("/export.csv")
def export_csv(db: Session = Depends(get_db)):
    from fastapi.responses import StreamingResponse
    import csv, io
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["child_id", "age_months", "weight_kg", "height_cm", "muac_cm", "status", "risk_score"])
    for v in db.query(Visit).all():
        writer.writerow([v.child_id, v.age_months, v.weight_kg, v.height_cm, v.muac_cm, v.status, v.risk_score])
    output.seek(0)
    return StreamingResponse(iter([output.getvalue()]), media_type="text/csv",
                             headers={"Content-Disposition": "attachment; filename=nutritrack_export.csv"})
