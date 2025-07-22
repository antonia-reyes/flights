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


@router.get("/{flight_id}", response_model=schema.Flight)
async def get_flight(flight_id: str):
    """Get a flight by ID."""
    flight = await crud.get_flight(flight_id)
    return flight


@router.post("/", response_model=schema.Flight)
async def create_flight(flight: schema.FlightCreate):
    """Create a flight."""
    flight_data = schema.Flight(**flight.model_dump())
    return await crud.create_flight(flight_data)


@router.put("/{flight_id}", response_model=schema.Flight)
async def update_flight(flight_id: str, flight: schema.FlightUpdate):
    """Update a flight."""
    return await crud.update_flight(flight_id, flight.model_dump())


@router.delete("/{flight_id}", response_model=bool)
async def delete_flight(flight_id: str):
    """Delete a flight."""
    return await crud.delete_flight(flight_id)