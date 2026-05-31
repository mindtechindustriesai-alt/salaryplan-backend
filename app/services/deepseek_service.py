"""DeepSeek API service with offline fallback"""

import httpx
from typing import Tuple
from app.config import settings
from app.services.knowledge_base import knowledge_base
from app.services.language_service import language_service


class DeepSeekService:
    """Service for DeepSeek API calls"""
    
    def __init__(self):
        self.api_key = settings.DEEPSEEK_API_KEY
        self.timeout = 60.0
    
    async def get_response(self, message: str, language: str, portal: str, system: str) -> Tuple[str, str]:
        """Get response from DeepSeek API"""
        
        if not self.api_key:
            return self.get_offline_response(message, language), "offline_kb_fallback"
        
        system_prompt = language_service.get_system_prompt(language, portal, system)
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    "https://api.deepseek.com/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "deepseek-chat",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": message}
                        ],
                        "temperature": 0.7,
                        "max_tokens": 2048
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    reply = data["choices"][0]["message"]["content"]
                    return reply, "luvuno_llm"
                else:
                    return self.get_offline_response(message, language), "api_error_fallback"
                    
        except Exception:
            return self.get_offline_response(message, language), "exception_fallback"
    
    def get_offline_response(self, message: str, language: str) -> str:
        """Get response from offline knowledge base"""
        answer = knowledge_base.get_answer(message)
        return language_service.translate_response(answer, language)


deepseek_service = DeepSeekService()
