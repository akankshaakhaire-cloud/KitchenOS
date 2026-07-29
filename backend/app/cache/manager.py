from redis.asyncio import Redis

from app.cache.connection import get_redis_client


class RedisManager:
    """
    Redis Connection Manager
    Responsible for managing Redis client lifecycle.
    """

    def __init__(self) -> None:
        self.client: Redis | None = None

    async def connect(self) -> None:
        """
        Connect to Redis server.
        """
        self.client = get_redis_client()

        # Verify connection
        await self.client.ping()

        print("✅ Redis Connected Successfully")

    async def disconnect(self) -> None:
        """
        Disconnect from Redis server.
        """
        if self.client is not None:
            await self.client.aclose()
            self.client = None

            print("🔴 Redis Connection Closed")


# Singleton Instance
redis_manager = RedisManager()