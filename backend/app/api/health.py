"""
Health check endpoints for KitchenOS.
"""

from fastapi import APIRouter

from app.cache.health import check_redis_health
from app.config.settings import settings
from app.schemas.response import ApiResponse

router = APIRouter(
    prefix="/api/v1/health",
    tags=["Health"],
)


@router.get("/", response_model=ApiResponse)
async def health_check():
    """
    Health check endpoint.
    """

    redis_health = await check_redis_health()

    return ApiResponse(
        message="KitchenOS is running successfully.",
        data={
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "status": "healthy",
            "services": {
                "redis": redis_health,
            },
        },
    )