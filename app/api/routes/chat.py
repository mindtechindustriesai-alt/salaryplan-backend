"""Chat routes with quantum verification"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.services.deepseek_service import deepseek_service
from app.services.quantum_service import quantum_service
from app.services.language_service import language_service
from app.core.constants import CHSH_SCORE

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    message: str
    portal: Optional[str] = "salaryplan"
    language: Optional[str] = "english"
    use_offline: Optional[bool] = False
    system: Optional[str] = "standard"


class ChatResponse(BaseModel):
    response: str
    portal: str
    language: str
    quantum_verified: bool
    chsh_score: float
    correlation: float
    source: str
    patent_number: str


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process chat message with quantum verification"""
    
    # Validate language
    lang = language_service.validate_language(request.language)
    
    # Get response from AI or offline fallback
    if request.use_offline:
        response = await deepseek_service.get_offline_response(request.message, lang)
        source = "offline_kb"
    else:
        response, source = await deepseek_service.get_response(
            request.message, 
            lang, 
            request.portal,
            request.system
        )
    
    # Get quantum verification
    quantum_data = quantum_service.verify_response()
    
    return ChatResponse(
        response=response,
        portal=request.portal,
        language=lang,
        quantum_verified=quantum_data["quantum_verified"],
        chsh_score=quantum_data["chsh_score"],
        correlation=quantum_data["correlation"],
        source=source,
        patent_number="2026/05142"
    )
