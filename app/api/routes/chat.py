from fastapi import APIRouter
from app.services.deepseek_service import deepseek_client

router = APIRouter()

@router.get("/chat")
async def chat(message: str):
    response = await deepseek_client.chat_completion(
        [{"role": "user", "content": message}]
    )
    return {
        "message": response["choices"][0]["message"]["content"],
        "quantum": {"chsh": 2.76, "patent": "SA 2026/05142"}
    }
