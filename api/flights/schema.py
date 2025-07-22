from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum


class FlightCategory(str, Enum):
    """Enum for flight passenger categories"""
    BLACK = "Black"
    PLATINUM = "Platinum"
    GOLD = "Gold"
    NORMAL = "Normal"


class PassengerBase(BaseModel):
    """Base schema for passenger"""
    id: int = Field(...)
    name: str = Field(...)
    hasConnections: bool = Field(...)
    age: int = Field(...)
    flightCategory: FlightCategory = Field(...)
    reservationId: str = Field(...)
    hasCheckedBaggage: bool = Field(...)


class PassengerCreate(PassengerBase):
    """Schema for creating a passenger"""
    pass



class FlightBase(BaseModel):
    """Base schema for flight"""
    flightCode: str = Field(...)
    passengers: List[PassengerBase] = Field(default=[])


class FlightCreate(BaseModel):
    """Schema for creating a flight"""
    flightCode: str = Field(...)
    passengers: List[PassengerCreate] = Field(default=[])


class FlightUpdate(BaseModel):
    """Schema for updating a flight"""
    flightCode: Optional[str] = Field(None)
    passengers: Optional[List[PassengerCreate]] = Field(None)


class Flight(FlightBase):
    """Schema for a flight"""

    class Config:
        from_attributes = True


