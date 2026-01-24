from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI(title="Entitlements Service")

class Entitlement(BaseModel):
    user_id: str
    feature_flags: list[str]

# Mock Database
db = {"user_123": ["premium_access", "api_export"]}

@app.get("/entitlements/{user_id}", response_model=Entitlement)
async def get_user_entitlements(user_id: str):
    """
    Retrieves specific feature permissions for a given user.
    Migrated from the monolithic 'UserPermissions' module.
    """
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"user_id": user_id, "feature_flags": db[user_id]}
