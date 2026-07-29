import json
from typing import Any

from redis.exceptions import RedisError

from app.cache.manager import redis_manager


class CacheService:
    """
    Generic Redis Cache Service.
    """

    async def set(
        self,
        key: str,
        value: Any,
        expire: int | None = None,
    ) -> bool:
        """
        Store value in Redis.
        """

        try:
            if redis_manager.client is None:
                return False

            serialized_value = json.dumps(value)

            await redis_manager.client.set(
                name=key,
                value=serialized_value,
                ex=expire,
            )

            return True

        except RedisError:
            return False

    async def get(self, key: str) -> Any | None:
        """
        Get value from Redis.
        """

        try:
            if redis_manager.client is None:
                return None

            value = await redis_manager.client.get(key)

            if value is None:
                return None

            return json.loads(value)

        except RedisError:
            return None

    async def delete(self, key: str) -> bool:
        """
        Delete cache key.
        """

        try:
            if redis_manager.client is None:
                return False

            await redis_manager.client.delete(key)

            return True

        except RedisError:
            return False

    async def exists(self, key: str) -> bool:
        """
        Check if key exists.
        """

        try:
            if redis_manager.client is None:
                return False

            return bool(await redis_manager.client.exists(key))

        except RedisError:
            return False

    async def expire(
        self,
        key: str,
        seconds: int,
    ) -> bool:
        """
        Set expiration time.
        """

        try:
            if redis_manager.client is None:
                return False

            return bool(
                await redis_manager.client.expire(
                    key,
                    seconds,
                )
            )

        except RedisError:
            return False

    async def clear(self) -> bool:
        """
        Clear current Redis database.
        """

        try:
            if redis_manager.client is None:
                return False

            await redis_manager.client.flushdb()

            return True

        except RedisError:
            return False


cache_service = CacheService()