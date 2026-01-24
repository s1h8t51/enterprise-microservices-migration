# Migration Phases: From Monolith to Microservices

To mitigate risk, we divided the migration into four distinct phases over a 6-month timeline.

### Phase 1: Preparation (Month 1)
* **Goal:** Establish the foundation.
* **Actions:** * Set up the Kubernetes cluster and CI/CD pipelines.
    * Implement the API Gateway (Nginx Ingress) in front of the Monolith.
    * Deploy the Telemetry service to begin baseline monitoring.

### Phase 2: The "Pilot" Service (Months 2-3)
* **Goal:** Extract the first service (Entitlements).
* **Actions:** * Use the **Strangler Fig Pattern** to route `/api/v1/entitlements` to the new service.
    * Implement **Shadow Writes**: Write data to both the Monolith DB and the new Entitlements DB.

### Phase 3: Scaling & Extraction (Months 4-5)
* **Goal:** Extract Access Control and Licensing.
* **Actions:** * Decompose the shared database into service-specific schemas.
    * Implement the **Saga Pattern** for cross-service transactions.

### Phase 4: Optimization & Cleanup (Month 6)
* **Goal:** Decommission the Monolith.
* **Actions:** * Final cutover of all traffic.
    * Shutdown legacy servers.
    * Final cost audit to confirm the $400k annual savings.
