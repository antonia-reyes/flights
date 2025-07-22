"""This module contains the CRUD operations for the flights API."""

from typing import Optional, List
from . import models, exceptions, schema
from bson import ObjectId


async def create_flight(flight_data: schema.FlightCreate) -> models.Flight:
    if await models.Flight.find_one(models.Flight.flightCode == flight_data.flightCode):
        raise exceptions.DuplicateFlightError()
    flight = models.Flight(**flight_data.model_dump())
    await flight.create()
    return flight


async def get_flight(flight_id: str) -> Optional[models.Flight]:
    flight = await models.Flight.get(ObjectId(flight_id))
    if not flight:
        raise exceptions.FlightNotFoundError()
    return flight


async def get_all_flights() -> List[models.Flight]:
    return await models.Flight.find_all().to_list()


async def update_flight(flight_id: str, flight_data: schema.FlightUpdate) -> Optional[models.Flight]:
    flight = await models.Flight.get(ObjectId(flight_id))
    if not flight:
        raise exceptions.FlightNotFoundError()
    await flight.set(flight_data.model_dump())
    return await models.Flight.get(ObjectId(flight_id))


async def delete_flight(flight_id: str) -> bool:
    flight = await models.Flight.get(ObjectId(flight_id))
    if not flight:
        raise exceptions.FlightNotFoundError()
    await flight.delete()
    return True