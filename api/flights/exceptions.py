""" This module contains the exceptions for the flights app. """

from fastapi import HTTPException, status
from pydantic import BaseModel


class FlightNotFoundError(HTTPException):
    """
    Exception raised when a flight is not found.
    """

    class FlightNotFoundErrorSchema(BaseModel):
        """
        Schema for the FlightNotFoundError exception.
        """

        detail: str = "Flight not found."

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=self.FlightNotFoundErrorSchema().detail,
        )


class DuplicateFlightError(HTTPException):
    """
    Exception raised when a flight with the same data already exists.
    """

    class DuplicateFlightErrorSchema(BaseModel):
        """
        Schema for the DuplicateFlightError exception.
        """

        detail: str = "A flight with the same data already exists."

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=self.DuplicateFlightErrorSchema().detail,
        )