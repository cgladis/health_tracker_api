from fastapi import FastAPI
from app.api import api_router
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)
