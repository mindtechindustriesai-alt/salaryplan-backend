"""
SalaryPlan Services Package
"""

from .deepseek_ai_service import deepseek_ai, get_deepseek_ai, DeepSeekAI
from .knowledge_base import KnowledgeBase, get_knowledge_base
from .language_service import LanguageService, get_language_service
from .quantum_service import QuantumService, get_quantum_service

__all__ = [
    "deepseek_ai",
    "get_deepseek_ai",
    "DeepSeekAI",
    "KnowledgeBase",
    "get_knowledge_base",
    "LanguageService",
    "get_language_service",
    "QuantumService",
    "get_quantum_service"
]
