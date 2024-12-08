from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT"))
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6380/0")
