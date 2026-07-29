from redis.asyncio import ConnectionPool, Redis

from app.config.settings import settings


_pool: ConnectionPool | None = None


def get_connection_pool() -> ConnectionPool:
    """
    Create and return a singleton Redis Connection Pool.
    """

    global _pool

    if _pool is None:
        _pool = ConnectionPool(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            username=settings.REDIS_USERNAME or None,
            password=settings.REDIS_PASSWORD or None,
            decode_responses=settings.REDIS_DECODE_RESPONSES,
            max_connections=20,
        )

    return _pool


def get_redis_client() -> Redis:
    """
    Return Redis client using connection pool.
    """

    return Redis(connection_pool=get_connection_pool())