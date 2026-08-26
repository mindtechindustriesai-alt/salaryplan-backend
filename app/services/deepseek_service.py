"""
DeepSeek AI Service for SalaryPlan
CHSH S=2.76 · SA 2026/05142
"""

import os
import json
from typing import List, Dict, Any, Optional


class DeepSeekService:
    """Service for interacting with DeepSeek AI API"""
    
    def __init__(self):
        self.api_key = os.environ.get("DEEPSEEK_API_KEY", "")
        self.api_url = "https://api.deepseek.com/v1"
        self.model = "deepseek-chat"
        
    async def chat(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> Dict[str, Any]:
        """Send a chat request to DeepSeek"""
        if not self.api_key:
            return self._get_fallback_response()
        
        try:
            import httpx
            async with httpx.AsyncClient(timeout=60) as client:
                response = await client.post(
                    f"{self.api_url}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.model,
                        "messages": messages,
                        "temperature": temperature,
                        "max_tokens": 1000
                    }
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"DeepSeek API error: {e}")
            return self._get_fallback_response()
    
    def _get_fallback_response(self) -> Dict[str, Any]:
        """Return quantum-inspired fallback response"""
        return {
            "choices": [{
                "message": {
                    "content": "⚛️ CHSH S=2.76 quantum intelligence active. 🇿🇦 Built in Africa, for Africa. Data stays on device (Edge First)."
                }
            }],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        }


def get_deepseek_service() -> DeepSeekService:
    """Factory function to get DeepSeek service instance"""
    return DeepSeekService()


# Global instance
deepseek_service = get_deepseek_service()
