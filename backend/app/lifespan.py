from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.cache.manager import redis_manager
from app.database.init_db import init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle events.
    """

    print("🚀 Starting KitchenOS...")

    # Initialize MongoDB
    await init_database()

    # Connect Redis
    await redis_manager.connect()

    print("✅ KitchenOS Started Successfully")

    yield

    print("🛑 Shutting Down KitchenOS...")

    # Disconnect Redis
    await redis_manager.disconnect()

    print("✅ KitchenOS Shutdown Successfully")