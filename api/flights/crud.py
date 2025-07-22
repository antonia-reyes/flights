"""This module contains the CRUD operations for the flights API."""

from typing import Optional, List
from . import models, exceptions, schema


async def create_flight(flight_data: schema.FlightCreate) -> models.Flight:
    if await models.Flight.find_one(models.Flight.flightCode == flight_data.flightCode):
        raise exceptions.DuplicateFlightError()
    flight = models.Flight(**flight_data.model_dump())
    await flight.create()
    return flight


async def get_flight_by_code(flight_code: str) -> Optional[models.Flight]:
    flight = await models.Flight.find_one(models.Flight.flightCode == flight_code)
    if not flight:
        raise exceptions.FlightNotFoundError()
    return flight


async def get_all_flights() -> List[models.Flight]:
    return await models.Flight.find_all().to_list()


async def update_flight(flight_code: str, flight_data: schema.FlightUpdate) -> Optional[models.Flight]:
    flight = await models.Flight.find_one(models.Flight.flightCode == flight_code)
    if not flight:
        raise exceptions.FlightNotFoundError()
    
    update_data = flight_data.model_dump(exclude_unset=True, exclude_none=True)
    
    if update_data:
        await flight.set(update_data)
    
    return flight


async def delete_flight(flight_code: str) -> bool:
    flight = await models.Flight.find_one(models.Flight.flightCode == flight_code)
    if not flight:
        raise exceptions.FlightNotFoundError()
    await flight.delete()
    return True