"""
Application-wide constants for KitchenOS.

This module contains reusable constant values used across the project.
Avoid hardcoding strings in the application.
"""

# ==========================================================
# Application
# ==========================================================

APP_TITLE = "KitchenOS"

API_PREFIX = "/api/v1"


# ==========================================================
# User Roles
# ==========================================================

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

ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"


# ==========================================================
# Soft Delete
# ==========================================================

NOT_DELETED = False
IS_DELETED = True