from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_health_score

router = APIRouter()


@router.get("/get_health_score/{user_id}")
def get_health_score_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_health_score(db, user_id)
