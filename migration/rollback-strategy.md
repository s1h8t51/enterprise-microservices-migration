----
# Rollback Strategy: The "Safety Net"

In an enterprise environment, "Move fast and break things" is not an option. We utilize a tiered rollback approach.

### Tier 1: Instant Traffic Reversion (Ingress Level)
If the error rate exceeds 1% during a deployment, the Ingress controller is configured to instantly point traffic back to the stable legacy endpoint.

### Tier 2: Database Reconciliation
Since we use **Dual-Writes**, the legacy database remains the "Source of Truth" during the migration. If a microservice fails, we can stop the sync and rely on the legacy DB without data loss.

### Tier 3: Version Rollback (K8s)
We maintain the last three successful container images in the registry.
```bash
# Emergency command to return to the previous stable state
kubectl rollout undo deployment/entitlements-service
