"""
SalaryPlan Models Package
Exports all Pydantic models for the MindTech financial intelligence platform.
"""

from .chat import ChatRequest, ChatResponse, Message
from .financial import (
    SalaryRequest, SalaryResponse,
    FixedExpense, FixedExpenseRequest,
    DailySpending, DailySpendingRequest,
    DebtSettlement, DebtSettlementRequest,
    LoanShark, LoanSharkPriority,
    BorrowLend, BorrowLendRequest,
    SavingsGoal, SavingsGoalRequest,
    AIInsight
)
from .quantum import (
    QuantumState, QuantumMeasurement,
    CHSHRequest, CHSHResponse,
    QuantumBadge
)
from .wages import (
    WageRequest, WageResponse,
    WeeklyBudget, WeeklyBudgetRequest,
    WageCalculation
)
from .reports import (
    ReportRequest, ReportResponse,
    FinancialSummary, SpendingBreakdown,
    DebtAnalysis, SavingsReport
)
from .user import (
    User, UserProfile, UserSettings,
    AuthRequest, AuthResponse,
    NotificationPreference
)
from .notifications import (
    Notification, NotificationRequest,
    PushNotification, Alert
)

__all__ = [
    # Chat models
    "ChatRequest", "ChatResponse", "Message",
    
    # Financial models
    "SalaryRequest", "SalaryResponse",
    "FixedExpense", "FixedExpenseRequest",
    "DailySpending", "DailySpendingRequest",
    "DebtSettlement", "DebtSettlementRequest",
    "LoanShark", "LoanSharkPriority",
    "BorrowLend", "BorrowLendRequest",
    "SavingsGoal", "SavingsGoalRequest",
    "AIInsight",
    
    # Quantum models
    "QuantumState", "QuantumMeasurement",
    "CHSHRequest", "CHSHResponse",
    "QuantumBadge",
    
    # Wages models
    "WageRequest", "WageResponse",
    "WeeklyBudget", "WeeklyBudgetRequest",
    "WageCalculation",
    
    # Reports models
    "ReportRequest", "ReportResponse",
    "FinancialSummary", "SpendingBreakdown",
    "DebtAnalysis", "SavingsReport",
    
    # User models
    "User", "UserProfile", "UserSettings",
    "AuthRequest", "AuthResponse",
    "NotificationPreference",
    
    # Notifications models
    "Notification", "NotificationRequest",
    "PushNotification", "Alert"
]
