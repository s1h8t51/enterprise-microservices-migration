# Service Interaction Flow

```mermaid
sequenceDiagram
    participant U as User
    participant G as API Gateway
    participant A as Access Control
    participant E as Entitlements
    participant T as Telemetry

    U->>G: Request Resource
    G->>A: Validate JWT
    A-->>G: Authorized
    G->>E: Check Permission (REST)
    E-->>G: Allowed
    G->>U: Deliver Resource
    G-)T: Log Usage Event (Async)
