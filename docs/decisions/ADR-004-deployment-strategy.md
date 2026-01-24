# ADR 004: Deployment and Release Strategy

## Status
Accepted

## Context
Downtime in the licensing system results in significant financial loss. We need a way to release code without impacting 100% of the user base simultaneously.

## Decision
We will utilize **Canary Deployments** via Kubernetes and an Ingress Controller (Nginx/Istio).

1.  **Traffic Split:** New versions receive 5% of traffic initially.
2.  **Validation:** Automated metrics (Error rate, Latency) are monitored for 10 minutes.
3.  **Promotion:** If healthy, traffic increases to 25%, then 100%. 
4.  **Feature Flags:** Use the Entitlements service to toggle high-risk features on/off without a redeploy.

## Consequences
* **Pros:** Minimal impact if a bug reaches production; allows for "testing in prod" with internal users.
* **Cons:** Requires sophisticated CI/CD pipelines and robust observability.
