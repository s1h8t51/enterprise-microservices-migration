# Rollback Strategy

## 1. Automated Health Checks
If the Error Rate (5xx) exceeds 1% during a canary deployment, the Ingress controller will automatically divert 100% of traffic back to the **Legacy Monolith**.

## 2. Database Versioning
* **Forward-Only Changes:** We avoid destructive schema changes (dropping columns) until the migration phase is 100% complete.
* **Toggle:** Each service includes a `USE_LEGACY_DB` environment variable to point back to the original source if the new microservice DB desyncs.

## 3. Communication
In the event of a rollback, the "On-Call" engineer must trigger the `rollback.sh` script, which resets the Kubernetes deployment to the previous `image_tag`.
