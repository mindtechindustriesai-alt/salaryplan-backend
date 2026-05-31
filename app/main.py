"""
SalaryPlan + Luvuno Quantum Backend
Africa's First Quantum-Verified Financial Intelligence Platform
Patent: South African Provisional Patent No. 2026/05142
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.api.routes import chat, financial, quantum, health
from app.api.middleware.logging import LoggingMiddleware
from app.api.middleware.rate_limit import RateLimitMiddleware
from app.core.constants import SERVICE_NAME, VERSION, PATENT_NUMBER, CHSH_SCORE


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║  {SERVICE_NAME} v{VERSION}                                      ║
    ║  Patent: {PATENT_NUMBER} (Filed 12 May 2026)                    ║
    ║  Quantum Verification: CHSH S={CHSH_SCORE} (98.4% correlation)  ║
    ║  IBM Job ID: d55p3jgnsj9s73b32lj0                              ║
    ║  ENSafrica Pro Bono · Dr Bernard Dippenaar                     ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    yield
    print("Shutting down...")


app = FastAPI(
    title=SERVICE_NAME,
    description="Quantum-verified financial intelligence API for SalaryPlan",
    version=VERSION,
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitMiddleware)

# Routes
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(quantum.router, prefix="/api", tags=["Quantum"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(financial.router, prefix="/api", tags=["Financial"])


@app.get("/")
async def root():
    return {
        "service": SERVICE_NAME,
        "version": VERSION,
        "status": "operational",
        "patent": {
            "number": PATENT_NUMBER,
            "filing_date": "2026-05-12",
            "attorney": "ENSafrica - Dr Bernard Dippenaar"
        },
        "quantum_verification": {
            "chsh_score": CHSH_SCORE,
            "correlation": settings.QUANTUM_CORRELATION,
            "violation_percentage": settings.VIOLATION_PERCENTAGE,
            "ibm_job_id": settings.IBM_JOB_ID
        },
        "supported_languages": settings.SUPPORTED_LANGUAGES,
        "endpoints": [
            "GET /",
            "GET /api/health",
            "GET /api/quantum/status",
            "POST /api/chat",
            "POST /api/financial/advice"
        ]
    }
