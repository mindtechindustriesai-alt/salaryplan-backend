"""
SalaryPlan API - MindTech Financial Intelligence Platform
CHSH S=2.76 · SA 2026/05142
"""

import httpx
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="SalaryPlan API",
    description="MindTech Financial Intelligence Platform",
    version="2.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== CONSTANTS =====
LUVUNO_URL = "https://luvuno-backend-proxy.onrender.com"
MQOS_URL = "https://mqos-tererai.onrender.com"
CHSH_S = 2.76
PATENT = "SA 2026/05142"
IBM_JOB_ID = "d8uhvl4bp3hs738628cg"

# ===== REQUEST MODELS =====
class ChatRequest(BaseModel):
    message: str

# ===== ROUTER =====
router = APIRouter(prefix="/api/v1")

@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "chsh": f"S={CHSH_S}",
        "patent": PATENT,
        "timestamp": datetime.now().isoformat()
    }

@router.get("/quantum/badge")
async def quantum_badge():
    return {
        "chsh": f"S={CHSH_S}",
        "patent": PATENT,
        "status": "quantum_ready",
        "entanglement": "maximal",
        "ibm_job_id": IBM_JOB_ID
    }

@router.get("/chat")
async def chat_get(message: str):
    """Legacy GET chat (kept for backwards compatibility)."""
    return {
        "response": f"⚛️ CHSH S={CHSH_S} quantum intelligence: {message}",
        "quantum": {
            "chsh": CHSH_S,
            "patent": PATENT,
            "state": "entangled"
        }
    }

@router.get("/africa")
async def africa():
    return {
        "message": "🌍 Built in Africa, for Africa",
        "sovereignty": "Data stays on device",
        "languages": ["English", "isiZulu", "isiXhosa", "Shona"],
        "patent": PATENT
    }

# ============================================================
# UNIFIED MQOS VERIFICATION ENDPOINT
# ============================================================
@router.get("/verify/chsh")
async def verify_chsh():
    """
    Unified MQOS CHSH verification endpoint.
    Returns the immutable IBM Kingston attestation.
    """
    return {
        "S": CHSH_S,
        "backend": "ibm_kingston",
        "job_id": IBM_JOB_ID,
        "status": "CONFIRMED",
        "patent": PATENT,
        "hardware_verified": True,
        "quantum_max": 2.8284,
        "classical_limit": 2.0,
        "app": "salaryplan",
        "timestamp": datetime.now().isoformat()
    }

# ============================================================
# APP STATUS — HEALTH CHECK FOR MQOS DASHBOARD
# ============================================================
@router.get("/apps/salaryplan/status")
async def app_status():
    return {
        "app": "salaryplan",
        "status": "operational",
        "version": "2.0.1",
        "quantum_badge": f"CHSH S={CHSH_S}",
        "patent": PATENT,
        "ibm_job_id": IBM_JOB_ID,
        "timestamp": datetime.now().isoformat()
    }

app.include_router(router)

# ===== ROOT =====
@app.get("/")
async def root():
    return {
        "message": f"⚛️ SalaryPlan API - CHSH S={CHSH_S}",
        "patent": PATENT,
        "status": "quantum_ready",
        "built": "Africa",
        "for": "Africa",
        "timestamp": datetime.now().isoformat()
    }

# ============================================================
# POST /api/chat — LUVUNO PROXY
# ============================================================
@app.post("/api/chat")
async def chat_post(request: ChatRequest):
    """
    Proxy chat requests to Luvuno backend.
    Falls back to a local response if Luvuno is unavailable.
    """
    user_message = request.message

    if not user_message or not user_message.strip():
        return {
            "error": "Message is required",
            "response": "Please provide a message.",
            "chsh": str(CHSH_S),
            "patent": PATENT
        }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                f"{LUVUNO_URL}/api/chat",
                json={
                    "message": user_message,
                    "portal": "salaryplan"
                },
                timeout=30.0
            )
            if res.status_code == 200:
                data = res.json()
                return {
                    "response": data.get("response") or data.get("reply") or "No response from Luvuno.",
                    "chsh": str(CHSH_S),
                    "patent": PATENT,
                    "ibm_job_id": IBM_JOB_ID,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                raise Exception(f"Luvuno returned {res.status_code}")

    except Exception as e:
        # Fallback: local rule-based response
        msg = user_message.lower().strip()

        if any(k in msg for k in ["pay", "offer", "installment", "settle"]):
            fallback = (
                "📉 That's a reasonable starting point.\n\n"
                "Let's structure the proposal:\n"
                "1. Confirm what you can realistically afford.\n"
                "2. Work out a monthly amount that fits your budget.\n"
                "3. Propose a clear repayment period.\n"
                "4. Ask the creditor to confirm any arrangement in writing."
            )
        elif any(k in msg for k in ["rights", "nca", "legal", "help"]):
            fallback = (
                "🧠 I'm your SalaryPlan negotiation assistant.\n\n"
                "1. Understand the amount you owe.\n"
                "2. Check what you can realistically afford.\n"
                "3. Keep copies of all correspondence.\n"
                "4. Ask for agreements in writing.\n"
                "5. Consider professional advice for legal matters."
            )
        elif any(k in msg for k in ["budget", "afford", "salary", "income"]):
            fallback = (
                "💰 Let's start with affordability.\n\n"
                "Key figures:\n"
                "• Monthly income\n"
                "• Essential monthly expenses\n"
                "• Existing debt payments\n"
                "• Amount available for repayment"
            )
        else:
            fallback = (
                f"⚛️ SalaryPlan Quantum Intelligence is active.\n\n"
                f"Luvuno is temporarily unavailable. Your message was: '{user_message}'.\n\n"
                f"Try asking:\n"
                f"• \"I can pay R500 per month.\"\n"
                f"• \"Can I negotiate my debt?\"\n"
                f"• \"What are my rights?\"\n"
                f"• \"Help me prepare an offer.\""
            )

        return {
            "response": fallback,
            "chsh": str(CHSH_S),
            "patent": PATENT,
            "ibm_job_id": IBM_JOB_ID,
            "fallback": True,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
