from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URL")

try:
    print("Connecting to MongoDB Atlas...")

    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=10000
    )

    client.admin.command("ping")

    print("✅ MongoDB Connected Successfully")

except Exception as e:
    print("❌ Connection Failed")
    print(e)