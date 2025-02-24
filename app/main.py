from fastapi import FastAPI
from app.api import api_router
from app.database import engine, Base

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(api_router)
