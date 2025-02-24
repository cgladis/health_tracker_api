from sqlalchemy.orm import Session
from models import Activity, Sleep, BloodTest, HealthScoreWeights
from sqlalchemy import and_


def get_health_score(db: Session, user_id: int):
    activities = db.query(Activity).filter(and_(Activity.user_id == user_id)).all()
    sleeps = db.query(Sleep).filter(and_(Sleep.user_id == user_id)).all()
    blood_tests = db.query(BloodTest).filter(and_(BloodTest.user_id == user_id)).all()
    weights = db.query(HealthScoreWeights).first()

    if not weights:
        raise ValueError("Health score weights are not set in the database. Please initialize them.")

    steps_avg = sum(a.steps for a in activities) / len(activities) if activities else 0
    sleep_avg = sum(s.duration for s in sleeps) / len(sleeps) if sleeps else 0
    glucose_avg = sum(b.glucose for b in blood_tests) / len(blood_tests) if blood_tests else 0

    score = (steps_avg / 10000) * weights.steps_weight + (sleep_avg / 8) * weights.sleep_weight + \
            ((100 - abs(90 - glucose_avg)) / 100) * weights.glucose_weight

    return {"user_id": user_id, "health_score": round(score * 100, 2)}
