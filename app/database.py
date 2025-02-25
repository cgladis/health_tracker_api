from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import Base, HealthScoreWeights
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

STEPS_WEIGHT = float(os.getenv("DEFAULT_STEPS_WEIGHT"))
SLEEP_WEIGHT = float(os.getenv("DEFAULT_SLEEP_WEIGHT"))
GLUCOSE_WEIGHT = float(os.getenv("DEFAULT_GLUCOSE_WEIGHT"))

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def initialize_health_score_weights():
    db: Session = SessionLocal()
    try:
        weights = db.query(HealthScoreWeights).first()
        if not weights:
            weights = HealthScoreWeights(
                steps_weight=STEPS_WEIGHT,
                sleep_weight=SLEEP_WEIGHT,
                glucose_weight=GLUCOSE_WEIGHT
            )
            db.add(weights)
            db.commit()
    finally:
        db.close()


initialize_health_score_weights()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
