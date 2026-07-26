from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings


client: AsyncIOMotorClient | None = None


def connect_to_mongodb() -> AsyncIOMotorClient:
    global client

    if client is None:
        client = AsyncIOMotorClient(settings.MONGODB_URL)

    return client


def get_database():
    if client is None:
        raise RuntimeError("MongoDB is not connected.")

    return client[settings.DATABASE_NAME]


def close_mongodb_connection():
    global client

    if client is not None:
        client.close()
        client = None