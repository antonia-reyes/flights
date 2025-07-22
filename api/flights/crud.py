"""This module contains the CRUD operations for the flights API."""

from typing import Optional, List
from .models import Flight
from bson import ObjectId


async def create_flight(flight_data: Flight) -> Flight:
    await flight_data.create()
    return flight_data


async def get_flight(flight_id: str) -> Optional[Flight]:
    return await Flight.get(ObjectId(flight_id))


async def get_all_flights() -> List[Flight]:
    return await Flight.find_all().to_list()


async def update_flight(flight_id: str, flight_data: dict) -> Optional[Flight]:
    flight = await Flight.get(ObjectId(flight_id))
    if not flight:
        return None
    await flight.set(flight_data)
    return await Flight.get(ObjectId(flight_id))


async def delete_flight(flight_id: str) -> bool:
    flight = await Flight.get(ObjectId(flight_id))
    if not flight:
        return False
    await flight.delete()
    return True