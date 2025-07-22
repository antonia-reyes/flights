"""This module contains the configuration variables for the application."""

import os
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    App settings class.
    """

    mongodb_url: str = os.getenv("MONGODB_URL")
    mongo_initdb_database: str = os.getenv("MONGO_INITDB_DATABASE")


@lru_cache
def get_settings() -> Settings:
    """
    Returns the app settings.
    """
    return Settings()