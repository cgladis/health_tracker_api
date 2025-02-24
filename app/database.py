from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, HealthScoreWeights

DATABASE_URL = "sqlite:///./health_tracker.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def initialize_health_score_weights():
    db: Session = SessionLocal()
    try:
        weights = db.query(HealthScoreWeights).first()
        if not weights:
            weights = HealthScoreWeights(steps_weight=0.4, sleep_weight=0.4, glucose_weight=0.2)
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
