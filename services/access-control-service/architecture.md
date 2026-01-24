# Access Control Architecture

## Strategy: Centralized Gateway + Local Validation
To prevent the "Chatty Service" problem (where every request results in a network call to this service), we use a hybrid approach:

1.  **Gateway Validation:** The API Gateway calls ACS to validate the JWT signature and expiration.
2.  **Claims Injection:** ACS injects user identity and roles into the request headers (e.g., `X-User-ID`, `X-User-Role`).
3.  **Downstream Trust:** Internal services trust the headers provided by the Gateway, reducing latency.

## Security Model
We utilize **RBAC (Role-Based Access Control)**. 
- **Roles:** Defined globally (e.g., `ORG_ADMIN`).
- **Permissions:** Linked to roles and checked within specific service logic.
