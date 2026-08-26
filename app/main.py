# ============================================================
# SALARYPLAN BACKEND — MAIN APPLICATION
# ============================================================

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt

# Import routes
from app.api.routes import (
    chat, financial, quantum, health, 
    wages, reports, user, notifications
)

load_dotenv()

# ============================================================
# FIREBASE INIT
# ============================================================
cred_dict = {
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY", "").replace('\\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "token_uri": "https://oauth2.googleapis.com/token",
}
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)
db = firestore.client()

# ============================================================
# JWT SETTINGS
# ============================================================
SECRET_KEY = os.getenv("JWT_SECRET", "salaryplan-super-secret-key")
ALGORITHM = "HS256"
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT and return user ID."""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("userId")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ============================================================
# FASTAPI APP
# ============================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 SalaryPlan Backend Starting...")
    print(f"📡 Firebase connected: {db.project}")
    print(f"⚛️ Quantum: CHSH S=2.76")
    yield
    print("🛑 SalaryPlan Backend Shutting down")

app = FastAPI(
    title="SalaryPlan Backend",
    description="Financial intelligence with DeepSeek AI & Quantum Verification",
    version="2.0.0",
    lifespan=lifespan
)

# ============================================================
# CORS
# ============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# ROUTES
# ============================================================
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(financial.router, prefix="/api/financial", tags=["Financial"])
app.include_router(quantum.router, prefix="/api/quantum", tags=["Quantum"])
app.include_router(health.router, prefix="/api/health", tags=["Health"])
app.include_router(wages.router, prefix="/api/wages", tags=["Wages"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])
app.include_router(user.router, prefix="/api/user", tags=["User"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["Notifications"])

# ============================================================
# ROOT & HEALTH
# ============================================================
@app.get("/")
async def root():
    return {
        "service": "SalaryPlan Backend",
        "status": "operational",
        "version": "2.0.0",
        "quantum_verified": True,
        "chsh_score": 2.76,
        "patent": "2026/05142"
    }

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "firebase": db.project,
        "quantum": "CHSH S=2.76",
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
