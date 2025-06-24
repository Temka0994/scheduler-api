from motor.motor_asyncio import AsyncIOMotorClient
from src.properties import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)

scheduler_db = client["scheduler"]

scheduler_collection = scheduler_db["notices"]
