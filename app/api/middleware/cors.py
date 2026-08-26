# ============================================================
# SALARYPLAN BACKEND — CORS MIDDLEWARE CONFIGURATION
# ============================================================

from fastapi.middleware.cors import CORSMiddleware
import os

# ============================================================
# CORS ORIGINS CONFIGURATION
# ============================================================

# Get allowed origins from environment variable
ALLOWED_ORIGINS = os.getenv("CORS_ORIGINS", "").split(",")

# If no origins are set in env, use defaults
if not ALLOWED_ORIGINS or ALLOWED_ORIGINS == [""]:
    ALLOWED_ORIGINS = [
        "https://salary-plan-app.onrender.com",
        "https://salaryplan-frontend.onrender.com",
        "https://pelo-app.onrender.com",
        "https://khensani-ai-homeschooling.onrender.com",
        "http://localhost:5500",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
    ]

# ============================================================
# CORS MIDDLEWARE FACTORY
# ============================================================

def setup_cors(app):
    """
    Configure CORS middleware for the FastAPI app.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
        allow_headers=[
            "Authorization",
            "Content-Type",
            "Accept",
            "Origin",
            "X-Requested-With",
        ],
        expose_headers=["Content-Disposition"],
        max_age=86400,  # 24 hours
    )
    
    return app

# ============================================================
# HELPER — CORS PREFLIGHT LOGGING (Optional)
# ============================================================

async def log_cors_headers(request, call_next):
    """
    Middleware to log CORS headers for debugging.
    Add this to main.py if needed: app.middleware("http")(log_cors_headers)
    """
    response = await call_next(request)
    
    # Log the origin if present
    origin = request.headers.get("origin")
    if origin:
        print(f"🔗 CORS Request from: {origin}")
    
    return response
