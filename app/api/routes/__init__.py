"""
SalaryPlan API Routes Package
Exports all route modules for the financial intelligence platform.
"""

from .chat import router as chat_router
from .financial import router as financial_router
from .quantum import router as quantum_router
from .health import router as health_router
from .wages import router as wages_router
from .reports import router as reports_router
from .user import router as user_router
from .notifications import router as notifications_router

__all__ = [
    "chat_router",
    "financial_router",
    "quantum_router",
    "health_router",
    "wages_router",
    "reports_router",
    "user_router",
    "notifications_router"
]
