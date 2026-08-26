# ============================================================
# SALARYPLAN BACKEND — LANGUAGE SERVICE
# ============================================================

from typing import Dict, Optional

# Language mappings
LANGUAGE_PROMPTS = {
    "english": "Respond in English. Be clear and professional.",
    "zulu": "Respond in isiZulu. Use appropriate greetings like 'Sawubona'. Be warm and culturally sensitive.",
    "xhosa": "Respond in isiXhosa. Use appropriate greetings like 'Molo'. Be warm and culturally sensitive.",
    "shona": "Respond in chiShona. Use appropriate greetings like 'Mhoro'. Be warm and culturally sensitive."
}

def get_language_prompt(language: str = "english") -> str:
    """Get the system prompt for a given language."""
    return LANGUAGE_PROMPTS.get(language.lower(), LANGUAGE_PROMPTS["english"])

def get_system_prompt(
    language: str = "english",
    portal: str = "salaryplan",
    system: str = ""
) -> str:
    """
    Build the full system prompt with language, portal, and quantum context.
    """
    base_prompt = f"You are SalaryPlan AI, a financial intelligence assistant for South Africans. Portal: {portal}. {get_language_prompt(language)}"
    
    if portal == "salaryplan":
        base_prompt += " You help users with budgeting, debt management, savings goals, and financial planning."
    elif portal == "pelo_safety":
        base_prompt += " You help users with community safety, emergency response, and crime prevention."
    elif portal == "quantum":
        base_prompt += " You are a quantum AI assistant with CHSH S=2.76 verification."
    
    if system == "quantumthink":
        base_prompt += " Break down complex problems into clear steps. Use format: Step 1, Step 2, Step 3, Summary."
    
    return base_prompt

# Export the service object that deepseek_service.py expects
class LanguageService:
    def get_system_prompt(self, language: str = "english", portal: str = "salaryplan", system: str = ""):
        return get_system_prompt(language, portal, system)
    
    def get_language_prompt(self, language: str = "english"):
        return get_language_prompt(language)

# Create the instance that is imported
language_service = LanguageService()
