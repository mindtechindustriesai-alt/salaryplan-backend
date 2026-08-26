"""
SalaryPlan Services Package
Exports all service modules for AI, knowledge, language, and quantum functionality.
CHSH S=2.76 · SA 2026/05142
"""

from .deepseek_service import deepseek_service, get_deepseek_service
from .knowledge_base import KnowledgeBase, get_knowledge_base
from .language_service import LanguageService, get_language_service
from .quantum_service import QuantumService, get_quantum_service

__all__ = [
    "deepseek_service",
    "get_deepseek_service",
    "KnowledgeBase",
    "get_knowledge_base",
    "LanguageService",
    "get_language_service",
    "QuantumService",
    "get_quantum_service"
]
