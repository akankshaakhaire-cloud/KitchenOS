from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ==========================================================
    # Application
    # ==========================================================
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str

    HOST: str
    PORT: int

    # ==========================================================
    # Security
    # ==========================================================
    SECRET_KEY: str
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # ==========================================================
    # MongoDB
    # ==========================================================
    MONGODB_URL: str
    DATABASE_NAME: str

    # ==========================================================
    # Redis
    # ==========================================================
    REDIS_URL: str

    # ==========================================================
    # Settings Configuration
    # ==========================================================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()