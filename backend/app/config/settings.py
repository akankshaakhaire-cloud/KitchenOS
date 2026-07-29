from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings
    Loads configuration from .env
    """

    # ==========================================================
    # Application
    # ==========================================================

    APP_NAME: str = "KitchenOS"
    APP_VERSION: str = "1.0.0"

    ENVIRONMENT: str = "development"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    API_V1_PREFIX: str = "/api/v1"

    DEBUG: bool = True

    # ==========================================================
    # Security
    # ==========================================================

    SECRET_KEY: str
    JWT_SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ==========================================================
    # MongoDB
    # ==========================================================

    MONGODB_URL: str
    DATABASE_NAME: str

    # ==========================================================
    # Redis
    # ==========================================================

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int = 0

    REDIS_USERNAME: str | None = None
    REDIS_PASSWORD: str | None = None

    REDIS_SSL: bool = False
    REDIS_DECODE_RESPONSES: bool = True

    # ==========================================================
    # Settings Configuration
    # ==========================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return cached application settings.
    """
    return Settings()


settings = get_settings()