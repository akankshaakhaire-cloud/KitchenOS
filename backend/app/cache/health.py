from redis.exceptions import RedisError

from app.cache.manager import redis_manager


async def check_redis_health() -> dict:
    """
    Check Redis server health.
    """

    try:
        if redis_manager.client is None:
            return {
                "status": "disconnected",
                "message": "Redis client is not initialized",
            }

        await redis_manager.client.ping()

        return {
            "status": "healthy",
            "message": "Redis connection successful",
        }

    except RedisError as exc:
        return {
            "status": "unhealthy",
            "message": str(exc),
        }