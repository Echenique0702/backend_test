from os import getenv
from pydantic_settings import BaseSettings

# Settings class to configure project environment variables
class Settings(BaseSettings):
    API_V1: str = '/api/v1'
    DB_HOST: str = getenv("DB_HOST")
    DB_NAME: str = getenv("DB_NAME")
    DB_USER: str = getenv("DB_USER")
    DB_PASSWORD: str = getenv("DB_PASSWORD")

    class Config:
        case_sensitive = True

settings = Settings()