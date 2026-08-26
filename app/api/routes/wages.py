from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from firebase_admin import firestore
import firebase_admin

router = APIRouter()
db = firebase_admin.firestore.client()

class WeeklyBudget(BaseModel):
    weeklyWage: float
    weeklyFixed: float
    weeklyLimit: float
    userId: str

class WageHistory(BaseModel):
    userId: str
    date: str
    weeklyWage: float
    weeklyFixed: float
    weeklyLimit: float
    surplus: float

@router.post("/calculate")
async def calculate_weekly_budget(budget: WeeklyBudget):
    """Calculate weekly budget and return surplus."""
    remaining = budget.weeklyWage - budget.weeklyFixed
    surplus = remaining - budget.weeklyLimit
    return {
        "weeklyWage": budget.weeklyWage,
        "weeklyFixed": budget.weeklyFixed,
        "weeklyRemaining": remaining,
        "weeklyLimit": budget.weeklyLimit,
        "surplus": surplus,
        "isSurplus": surplus >= 0,
        "advice": f"You have R{abs(surplus)} {'to save' if surplus >= 0 else 'shortfall'}"
    }

@router.post("/save")
async def save_weekly_budget(budget: WeeklyBudget):
    """Save weekly budget settings to Firestore."""
    doc_ref = db.collection('wages').document(budget.userId)
    doc_ref.set({
        "weeklyWage": budget.weeklyWage,
        "weeklyFixed": budget.weeklyFixed,
        "weeklyLimit": budget.weeklyLimit,
        "updatedAt": datetime.utcnow().isoformat()
    }, merge=True)
    return {"status": "saved", "userId": budget.userId}

@router.get("/history/{userId}")
async def get_wage_history(userId: str):
    """Get user's wage history."""
    docs = db.collection('wages').where('userId', '==', userId).order_by('date', direction='DESCENDING').limit(10).get()
    return [doc.to_dict() for doc in docs]
