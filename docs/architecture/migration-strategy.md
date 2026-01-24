# Migration Strategy: The Strangler Fig Pattern

To ensure zero downtime for our enterprise clients, we utilized the **Strangler Fig Pattern**.

### Phase 1: The Proxy (API Gateway)
We introduced an Ingress controller to route traffic. Initially, 100% of traffic went to the Monolith.

### Phase 2: Incrementally Decoupling
1. **Entitlements** was the first service extracted due to its high change frequency.
2. We implemented **Dual-Writes**: Data was written to both the legacy DB and the new service DB to ensure consistency.

### Phase 3: Traffic Shifting
We used Canary releases (5% -> 25% -> 100%) to shift traffic to the new microservices.

### Phase 4: Decommissioning
Once metrics confirmed stability, the monolithic modules were disabled.
