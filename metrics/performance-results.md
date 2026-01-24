# Performance Results: Monolith vs. Microservices

This document summarizes the technical performance gains achieved through the migration. All metrics were collected using **Prometheus** and validated via **k6** load tests.

### 1. API Latency (p95)
We observed a significant reduction in response times, particularly for the Entitlements and Licensing endpoints, due to database decoupling and Redis caching.

| Endpoint | Monolith (Before) | Microservices (After) | Improvement |
| :--- | :--- | :--- | :--- |
| `/get-entitlements` | 450ms | 45ms | 90% Faster |
| `/validate-license` | 820ms | 120ms | 85% Faster |
| `/ingest-telemetry` | 1.2s | 30ms (Async) | 97% Faster |

### 2. Throughput (Requests Per Second)
The monolith struggled with vertical scaling limits. The new architecture scales horizontally across Kubernetes nodes.

* **Monolith Max Capacity:** 1,200 RPS (System-wide degradation occurs)
* **Microservices Capacity:** 15,000+ RPS (Scales linearly with Pod replicas)

### 3. Resource Efficiency
By isolating the **Telemetry Service**, we prevented usage spikes from consuming the CPU cycles needed for the **Licensing Service**.
- **CPU Utilization:** Reduced by 30% on average due to optimized Python 3.12 runtimes.
- **Memory Footprint:** Individual services run in lightweight <512MB containers.
