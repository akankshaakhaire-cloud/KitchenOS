"""
Application Enums for KitchenOS.

This module contains all common enums used across the project.
"""

from enum import Enum


# ==========================================================
# User Roles
# ==========================================================

class UserRole(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    CHEF = "CHEF"
    CASHIER = "CASHIER"
    WAITER = "WAITER"
    CUSTOMER = "CUSTOMER"


# ==========================================================
# Restaurant Status
# ==========================================================

class RestaurantStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


# ==========================================================
# Soft Delete Status
# ==========================================================

class DeleteStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"