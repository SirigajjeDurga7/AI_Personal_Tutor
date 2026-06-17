from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGODB_URL:
    raise RuntimeError("MONGODB_URL is not set. Ensure backend/.env exists and contains MONGODB_URL.")

if not DATABASE_NAME:
    raise RuntimeError("DATABASE_NAME is not set. Ensure backend/.env exists and contains DATABASE_NAME.")

client = AsyncIOMotorClient(MONGODB_URL)

db = client[DATABASE_NAME]