def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_login_success(client):
    response = client.post("/login", json={"username": "demo", "password": "nutri-demo"})
    assert response.status_code == 200

def test_login_failure(client):
    assert client.post("/login", json={"username": "x", "password": "x"}).status_code == 401

def test_create_child_and_visit(client):
    child = client.post("/children", json={"child_code": "C-1", "name": "Demo Child", "age_months": 24, "sex": "F"})
    assert child.status_code == 200
    visit = client.post("/visits", json={"child_id": child.json()["id"], "age_months": 24,
        "weight_kg": 10, "height_cm": 80, "muac_cm": 13, "dietary_diversity": 5, "recent_illness": 0})
    assert visit.status_code == 200
    assert "risk_score" in visit.json()

def test_missing_child(client):
    response = client.post("/visits", json={"child_id": 999, "age_months": 20,
        "weight_kg": 8, "height_cm": 70, "muac_cm": 12})
    assert response.status_code == 404

def test_dashboard_and_csv(client):
    assert client.get("/dashboard").status_code == 200
    assert "text/csv" in client.get("/export.csv").headers["content-type"]
