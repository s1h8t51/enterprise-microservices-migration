# Telemetry Service Architecture

## The "Write-Heavy" Design
Unlike the Entitlements service which is "Read-Heavy," Telemetry must handle thousands of writes per second. 

### Pipeline Flow:
1.  **Async Buffer:** Services do not wait for a response from Telemetry. They push events to a message queue.
2.  **Worker Pool:** A set of background workers consumes messages from the queue.
3.  **Time-Series Partitioning:** Data is stored in **TimescaleDB** using "hypertables" partitioned by time (e.g., daily chunks) to ensure query performance doesn't degrade as data grows.
4.  **Prometheus Integration:** Custom business metrics (e.g., `licenses_validated_total`) are exposed via a `/metrics` endpoint for long-term retention in Prometheus.

## Data Retention Policy
- **Raw Events:** Retained for 30 days.
- **Aggregated Metrics:** Retained for 1 year for business impact reporting.
