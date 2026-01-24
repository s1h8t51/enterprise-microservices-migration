# System Architecture Overview

## Current State
We have successfully transitioned from a single tiered Monolith to a **Cloud-Native Microservices** architecture running on Kubernetes.

### Architecture Components
* **API Gateway (Nginx Ingress):** Acts as the entry point, handling SSL termination and routing.
* **Service Layer:** Containerized Python/FastAPI services.
* **Event Bus (RabbitMQ):** Facilitates asynchronous communication between services to maintain eventual consistency.
* **Observability Stack:** Prometheus for metrics and Grafana for visualization.

## Data Flow
1.  **Ingress** receives a request and validates the JWT via the **Access Control Service**.
2.  The request is routed to the target service (e.g., **Entitlements**).
3.  Services emit events to the **Event Bus** for side effects (e.g., "License Used" -> **Telemetry**).
