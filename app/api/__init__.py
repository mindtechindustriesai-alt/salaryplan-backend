"""
SalaryPlan API Package
Exports the router aggregator for all API endpoints.
"""

from fastapi import APIRouter

from .routes import (
    chat_router,
    financial_router,
    quantum_router,
    health_router,
    wages_router,
    reports_router,
    user_router,
    notifications_router
)
from .middleware import cors_middleware, auth_middleware, rate_limit_middleware

# Create main API router
api_router = APIRouter(prefix="/api/v1")

# Register all route modules
api_router.include_router(chat_router, prefix="/chat", tags=["Chat"])
api_router.include_router(financial_router, prefix="/financial", tags=["Financial"])
api_router.include_router(quantum_router, prefix="/quantum", tags=["Quantum"])
api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(wages_router, prefix="/wages", tags=["Wages"])
api_router.include_router(reports_router, prefix="/reports", tags=["Reports"])
api_router.include_router(user_router, prefix="/user", tags=["User"])
api_router.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])

# Export middleware and router
__all__ = [
    "api_router",
    "cors_middleware",
    "auth_middleware",
    "rate_limit_middleware",
    "chat_router",
    "financial_router",
    "quantum_router",
    "health_router",
    "wages_router",
    "reports_router",
    "user_router",
    "notifications_router"
]
