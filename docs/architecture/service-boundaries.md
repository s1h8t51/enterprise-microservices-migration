# Service Boundaries & Bounded Contexts

Our decomposition strategy followed **Domain-Driven Design (DDD)** principles to ensure high cohesion and low coupling.

### 1. Entitlements Context
* **Responsibility:** Mapping users to "Rights" (e.g., Can this user export PDF?).
* **Data Owner:** `entitlements_db`
* **Reason for Split:** High frequency of updates due to marketing campaigns and tiered feature releases.

### 2. Licensing Context
* **Responsibility:** Legal contract enforcement, expiration dates, and key generation.
* **Data Owner:** `licensing_db`
* **Reason for Split:** High security and audit requirements; needs to be isolated from general usage tracking.

### 3. Telemetry Context
* **Responsibility:** High-volume event ingestion for system usage.
* **Data Owner:** Time-series database (e.g., InfluxDB/Prometheus).
* **Reason for Split:** Resource intensive; needs independent scaling to prevent usage spikes from crashing the checkout/licensing flow.
