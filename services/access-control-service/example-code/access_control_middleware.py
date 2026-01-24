from fastapi import Request, HTTPException, status
from typing import Optional
import time

class AccessControlMiddleware:
    """
    Simulates the logic used by the API Gateway or individual services
    to ensure the user is authenticated before hitting business logic.
    """
    async def __call__(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication credentials were not provided"
            )

        # In a real system, you would decode the JWT and check the 'exp' claim
        # Example validation logic:
        user_info = self.decode_and_verify(token)
        
        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or expired token"
            )

        # Inject user identity into request state for the controller to use
        request.state.user = user_info
        
        response = await call_next(request)
        return response

    def decode_and_verify(self, token: str) -> Optional[dict]:
        # Placeholder for JWT decoding logic (using PyJWT or similar)
        if "valid-token" in token:
            return {"uid": "user_99", "role": "admin", "tenant": "enterprise_corp"}
        return None
