# SalaryPlan + Luvuno Quantum Backend

## Africa's First Quantum-Verified Financial Intelligence Platform

### Patent Information
- **South African Provisional Patent No. 2026/05142**
- **Filed:** 12 May 2026
- **Attorney:** ENSafrica — Dr Bernard Dippenaar
- **Status:** Pending

### Quantum Verification
- **CHSH S=2.76** (38% above classical bound S=2.0)
- **Correlation:** 98.4%
- **IBM Verified:** Job ID `d55p3jgnsj9s73b32lj0`

### Features
- ✅ Quantum-verified AI financial advice
- ✅ Multi-language support (English, isiZulu, isiXhosa, chiShona)
- ✅ Offline knowledge base fallback
- ✅ Enterprise-grade security
- ✅ Rate limiting & request logging

### Tech Stack
- FastAPI (Python 3.11)
- DeepSeek API
- Render (deployment)
- Pydantic for validation

### Deployment

```bash
# Clone repository
git clone https://github.com/mindtech/salaryplan-backend.git

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your DEEPSEEK_API_KEY

# Run locally
uvicorn app.main:app --reload --port 8000

# Run with Docker
docker-compose up --build