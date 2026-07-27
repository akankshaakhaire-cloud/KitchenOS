from datetime import UTC, datetime

from beanie import Document
from pydantic import Field


class BaseDocument(Document):
    """
    Base document for all MongoDB collections.
    Contains common fields shared across all models.
    """

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    is_deleted: bool = False

    class Settings:
        is_root = True