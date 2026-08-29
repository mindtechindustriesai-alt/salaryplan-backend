# ============================================================
#  ADD THIS ROUTE — POST /api/chat (matches frontend)
# ============================================================

from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat_post(request: ChatRequest):
    user_message = request.message
    
    if not user_message:
        return {"error": "Message is required"}, 400
    
    # Your AI logic here — for now, a placeholder
    response_text = f"⚛️ CHSH S=2.76 quantum intelligence active. You said: '{user_message}'. I'm a negotiation simulator. Try structuring your offer."
    
    return {
        "response": response_text,
        "chsh": "2.76",
        "patent": "SA 2026/05142",
        "timestamp": datetime.now().isoformat()
    }
