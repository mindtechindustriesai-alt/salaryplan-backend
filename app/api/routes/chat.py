from fastapi import APIRouter, HTTPException
from typing import Optional
from app.services import deepseek_ai

router = APIRouter()

@router.get("/chat")
async def chat_endpoint(message: str, temperature: Optional[float] = 0.7):
    """Chat with DeepSeek AI"""
    try:
        response = await deepseek_ai.chat(
            [{"role": "user", "content": message}],
            temperature=temperature
        )
        return {
            "response": response.get("choices", [{}])[0].get("message", {}).get("content", ""),
            "quantum": {"chsh": 2.76, "patent": "SA 2026/05142"}
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
