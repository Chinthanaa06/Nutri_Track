from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True)
    child_code = Column(String(40), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    age_months = Column(Integer, nullable=False)
    sex = Column(String(10), nullable=False)
    visits = relationship("Visit", back_populates="child", cascade="all, delete-orphan")

class Visit(Base):
    __tablename__ = "visits"
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey("children.id"), nullable=False)
    recorded_at = Column(DateTime, default=datetime.utcnow)
    age_months = Column(Integer, nullable=False)
    weight_kg = Column(Float, nullable=False)
    height_cm = Column(Float, nullable=False)
    muac_cm = Column(Float, nullable=False)
    dietary_diversity = Column(Integer, default=0)
    recent_illness = Column(Integer, default=0)
    waz = Column(Float, nullable=False)
    haz = Column(Float, nullable=False)
    whz = Column(Float, nullable=False)
    status = Column(String(60), nullable=False)
    risk_score = Column(Float, nullable=False)
    child = relationship("Child", back_populates="visits")
