from fastapi import Request, HTTPException
import httpx

# The Access Control Service often acts as a gatekeeper
async def verify_authorization(request: Request):
    """
    Middleware to verify JWT and check basic access levels.
    Demonstrates the boundary between Identity and Feature Entitlement.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing Auth Header")

    # In a real scenario, this would call the Access Control Service API
    # or validate a signature locally.
    if "Bearer valid-token" not in auth_header:
        raise HTTPException(status_code=403, detail="Invalid Token")
    
    return True
