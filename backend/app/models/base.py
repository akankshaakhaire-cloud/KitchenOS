from datetime import datetime, UTC

from beanie import Document
from pydantic import Field


class BaseDocument(Document):
    """
    Base document for all MongoDB models.
    """

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    is_deleted: bool = False

    class Settings:
        is_root = True