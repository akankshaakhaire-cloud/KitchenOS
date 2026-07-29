"""
Custom exceptions for KitchenOS.

This module contains application-specific exceptions that can be
raised throughout the project.
"""

from fastapi import HTTPException, status


class KitchenOSException(HTTPException):
    """
    Base exception for KitchenOS.
    """

    def __init__(
        self,
        status_code: int,
        detail: str,
    ):
        super().__init__(
            status_code=status_code,
            detail=detail,
        )


class BadRequestException(KitchenOSException):
    """
    400 Bad Request
    """

    def __init__(self, detail: str = "Bad Request"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )


class UnauthorizedException(KitchenOSException):
    """
    401 Unauthorized
    """

    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        )


class ForbiddenException(KitchenOSException):
    """
    403 Forbidden
    """

    def __init__(self, detail: str = "Forbidden"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )


class NotFoundException(KitchenOSException):
    """
    404 Not Found
    """

    def __init__(self, detail: str = "Resource Not Found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class ConflictException(KitchenOSException):
    """
    409 Conflict
    """

    def __init__(self, detail: str = "Conflict"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
        )


class InternalServerException(KitchenOSException):
    """
    500 Internal Server Error
    """

    def __init__(self, detail: str = "Internal Server Error"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )