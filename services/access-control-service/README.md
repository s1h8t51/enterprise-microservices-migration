# Access Control Service (ACS)

## Purpose
The Access Control Service is the centralized authority for Identity and Access Management (IAM). It validates tokens, manages user sessions, and defines roles (RBAC).

## Core Responsibilities
- **Authentication:** Validating JWTs (JSON Web Tokens) issued by the Identity Provider.
- **Authorization:** Checking if a user's role (Admin, Editor, Viewer) matches the requested action.
- **Token Introspection:** Providing metadata about the current session to other microservices.

## Tech Stack
- **Framework:** FastAPI
- **Security:** OAuth2 / OpenID Connect (OIDC)
- **Data Store:** Redis (for session blacklisting and rapid role lookups)
