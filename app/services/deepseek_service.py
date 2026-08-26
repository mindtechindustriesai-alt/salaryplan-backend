# ============================================================
# SALARYPLAN BACKEND — DEEPSEEK SERVICE
# ============================================================

import os
import httpx
from typing import Optional, Dict, Any
from app.services.language_service import language_service

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

async def call_deepseek(
    prompt: str,
    language: str = "english",
    portal: str = "salaryplan",
    system: str = "",
    temperature: float = 0.5,
    max_tokens: int = 2048
) -> str:
    """
    Call DeepSeek API with the given prompt and parameters.
    """
    if not DEEPSEEK_API_KEY:
        return "DeepSeek API key not configured. Please set DEEPSEEK_API_KEY environment variable."
    
    try:
        # Build system prompt using language service
        system_prompt = language_service.get_system_prompt(language, portal, system)
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                DEEPSEEK_URL,
                headers={
                    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": temperature,
                    "max_tokens": max_tokens
                }
            )
            
            if response.status_code != 200:
                return f"DeepSeek API error: {response.status_code}"
            
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "No response")
            
    except httpx.TimeoutException:
        return "DeepSeek API timeout. Please try again."
    except Exception as e:
        return f"Error calling DeepSeek: {str(e)}"

# For backward compatibility
deepseek_service = {
    "call_deepseek": call_deepseek
}
