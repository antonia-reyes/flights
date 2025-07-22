""" Main module for the FastAPI application. """

from fastapi import FastAPI
from flights.endpoints import router as flights_router
from flights.models import Flight
from config import get_settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

app.include_router(flights_router)


@app.get("/")
def read_root():
    """Default route for the FastAPI application"""
    return {"message": "Hello, World!"}


@app.on_event("startup")
async def on_startup():
    """Initialize Beanie and connect to MongoDB."""
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongodb_url)
    await init_beanie(
        database=client[settings.mongo_initdb_database],
        document_models=[Flight],
    )