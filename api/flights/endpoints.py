"""This module contains the endpoints for the flights API."""

from fastapi import APIRouter
from typing import List
from . import crud, schema


router = APIRouter(
    prefix="/flights",
    tags=["flights"],
)


@router.get("/", response_model=List[schema.Flight])
async def get_flights():
    """Get all flights."""
    flights = await crud.get_all_flights()
    return flights


@router.get("/{flight_code}", response_model=schema.Flight)
async def get_flight(flight_code: str):
    """Get a flight by ID."""
    flight = await crud.get_flight(flight_code)
    return flight


@router.post("/", response_model=schema.Flight)
async def create_flight(flight: schema.FlightCreate):
    """Create a flight."""
    return await crud.create_flight(flight)


@router.put("/{flight_code}", response_model=schema.Flight)
async def update_flight(flight_code: str, flight: schema.FlightUpdate):
    """Update a flight."""
    return await crud.update_flight(flight_code, flight)


@router.delete("/{flight_code}", response_model=bool)
async def delete_flight(flight_code: str):
    """Delete a flight."""
    return await crud.delete_flight(flight_code)