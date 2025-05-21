from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

class Settings(BaseSettings):
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    ES_HOST: str = os.getenv("ES_HOST")
    ES_USER: str = os.getenv("ES_USER")
    ES_PASSWORD: str = os.getenv("ES_PASSWORD")
    ES_INDEX: str = os.getenv("ES_INDEX")
    BASE_URL: str = os.getenv("BASE_URL")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL")
    VERIFY_CERTS: bool = os.getenv("VERIFY_CERTS", "false").lower() == "true"

settings = Settings()