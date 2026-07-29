from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.health import router as health_router
from app.config.settings import settings
from app.database.connection import close_mongodb_connection
from app.database.database import init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events.
    """

    # Startup
    await init_database()

    yield

    # Shutdown
    close_mongodb_connection()


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


@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }