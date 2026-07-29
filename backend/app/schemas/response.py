"""
Standard API response schemas for KitchenOS.
"""

from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    """
    Standard API success response.
    """

    success: bool = True
    message: str
    data: Any | None = None


class ErrorResponse(BaseModel):
    """
    Standard API error response.
    """

    success: bool = False
    message: str
    error: Any | None = None