from typing import List
from enum import Enum
from pydantic import BaseModel, Field
from beanie import Document


class FlightCategory(str, Enum):
    BLACK = "Black"
    PLATINUM = "Platinum"
    GOLD = "Gold"
    NORMAL = "Normal"


class Passenger(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    hasConnections: bool = Field(...)
    age: int = Field(...)
    flightCategory: FlightCategory = Field(...)
    reservationId: str = Field(...)
    hasCheckedBaggage: bool = Field(...)


class Flight(Document):
    flightCode: str = Field(...)
    passengers: List[Passenger] = Field(default=[])

    class Settings:
        name = "flights"
