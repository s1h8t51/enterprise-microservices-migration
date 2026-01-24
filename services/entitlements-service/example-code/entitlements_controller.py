from fastapi import FastAPI, Depends, HTTPException
from typing import List
import os

app = FastAPI()

# In a real scenario, these would be fetched from a DB/Cache
MOCK_DATA = {
    "user_1": ["dashboard_view", "basic_reports"],
    "user_2": ["dashboard_view", "advanced_analytics", "export_csv"]
}

@app.get("/v1/users/{user_id}/features")
async def get_features(user_id: str):
    """
    Business Logic: Checks the user's current entitlements.
    Integration point for the 'Strangler Fig' pattern.
    """
    # 1. Check local cache (Redis)
    # 2. Fallback to Database if cache miss
    features = MOCK_DATA.get(user_id)
    
    if not features:
        raise HTTPException(status_code=404, detail="User entitlements not found")
        
    return {
        "user_id": user_id,
        "features": features,
        "environment": os.getenv("APP_ENV", "production")
    }

@app.post("/v1/internal/refresh-cache")
async def refresh_cache(user_id: str):
    """
    Triggered by an Event Consumer when a license is upgraded.
    """
    # Logic to invalidate Redis would go here
    return {"status": "cache_invalidated", "user_id": user_id}
