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
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    hasConnections: bool = Field(...)
    age: int = Field(..., gt=0)
    flightCategory: FlightCategory = Field(...)
    reservationId: str = Field(..., min_length=1)
    hasCheckedBaggage: bool = Field(...)


class Flight(Document):
    flightCode: str = Field(..., min_length=1)
    passengers: List[Passenger] = Field(default=[])

    class Settings:
        name = "flights"
