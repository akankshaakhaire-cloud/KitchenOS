from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.cache import router as cache_router
from app.api.health import router as health_router
from app.cache.manager import redis_manager
from app.config.settings import settings
from app.database.connection import close_mongodb_connection
from app.database.database import init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events.
    """

    # ==========================
    # Startup
    # ==========================

    print("🚀 Starting KitchenOS...")

    # Initialize MongoDB
    await init_database()

    # Connect Redis
    await redis_manager.connect()

    print("✅ KitchenOS Started Successfully")

    yield

    # ==========================
    # Shutdown
    # ==========================

    print("🛑 Shutting Down KitchenOS...")

    # Disconnect Redis
    await redis_manager.disconnect()

    # Close MongoDB
    close_mongodb_connection()

    print("✅ KitchenOS Shutdown Successfully")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production Ready Cloud Kitchen Management System",
    lifespan=lifespan,
)

# ==========================
# API Routers
# ==========================

app.include_router(health_router)
app.include_router(cache_router)


@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }