## 3. Testing Strategy: `migration/testing-strategy.md`



```markdown
# Testing Strategy for Distributed Systems

Transitioning to microservices required a shift from Monolithic Unit Testing to a **Distributed Testing Pyramid**.

### 1. Contract Testing (Pact)
We use contract tests to ensure that changes in the **Licensing Service** don't break the **Entitlements Service**. If the API contract changes, the CI build fails immediately.

### 2. Shadow Testing (Traffic Mirroring)
Before going live, we "mirrored" 10% of production traffic to the new services. We compared the outputs of the Monolith vs. the Microservice. If the results didn't match, we investigated without affecting the user.

### 3. Load Testing
Using **k6**, we simulated 5x our peak traffic to ensure the **Telemetry Service** could handle the ingestion volume without bottlenecking the system.
