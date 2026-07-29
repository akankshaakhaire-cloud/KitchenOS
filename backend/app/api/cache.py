from fastapi import APIRouter

from app.cache.cache_service import cache_service
from app.schemas.response import ApiResponse

router = APIRouter(
    prefix="/api/v1/cache",
    tags=["Cache"],
)


@router.post("/set", response_model=ApiResponse)
async def set_cache():
    """
    Store sample data in Redis.
    """

    data = {
        "restaurant": "Abhi's Kitchen",
        "city": "Pune",
        "status": "Active",
    }

    success = await cache_service.set(
        key="restaurant:1",
        value=data,
        expire=300,
    )

    return ApiResponse(
        message="Cache stored successfully.",
        data={
            "success": success,
        },
    )


@router.get("/get", response_model=ApiResponse)
async def get_cache():
    """
    Get cached data.
    """

    data = await cache_service.get("restaurant:1")

    return ApiResponse(
        message="Cache fetched successfully.",
        data=data,
    )


@router.delete("/delete", response_model=ApiResponse)
async def delete_cache():
    """
    Delete cached data.
    """

    success = await cache_service.delete("restaurant:1")

    return ApiResponse(
        message="Cache deleted successfully.",
        data={
            "success": success,
        },
    )


@router.get("/exists", response_model=ApiResponse)
async def exists_cache():
    """
    Check whether cache exists.
    """

    exists = await cache_service.exists("restaurant:1")

    return ApiResponse(
        message="Cache existence checked.",
        data={
            "exists": exists,
        },
    )