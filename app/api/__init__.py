from fastapi import APIRouter
from app.api.endpoints import router as health_router

api_router = APIRouter()
api_router.include_router(health_router, prefix="/api")
