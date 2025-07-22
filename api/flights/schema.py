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
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    hasConnections: bool = Field(...)
    age: int = Field(..., gt=0)
    flightCategory: FlightCategory = Field(...)
    reservationId: str = Field(..., min_length=1)
    hasCheckedBaggage: bool = Field(...)


class PassengerCreate(PassengerBase):
    """Schema for creating a passenger"""
    pass



class FlightBase(BaseModel):
    """Base schema for flight"""
    flightCode: str = Field(..., min_length=1)
    passengers: List[PassengerBase] = Field(default=[])


class FlightCreate(BaseModel):
    """Schema for creating a flight"""
    flightCode: str = Field(..., min_length=1)
    passengers: List[PassengerCreate] = Field(default=[])


class FlightUpdate(BaseModel):
    """Schema for updating a flight"""
    flightCode: Optional[str] = Field(None, min_length=1)
    passengers: Optional[List[PassengerCreate]] = Field(None)


class Flight(FlightBase):
    """Schema for a flight"""

    class Config:
        from_attributes = True


