# Telemetry Service

## Purpose
The Telemetry Service is responsible for the ingestion, processing, and storage of system-wide usage events and performance metrics. It provides the data necessary for billing, auditing, and real-time monitoring.

## Core Responsibilities
- **Event Ingestion:** Capturing high-volume "heartbeat" and "usage" events from other services.
- **Metrics Aggregation:** Transforming raw events into actionable time-series data.
- **Data Export:** Providing endpoints for Prometheus scraping and Grafana dashboards.

## Tech Stack
- **Framework:** FastAPI
- **Ingestion:** RabbitMQ / Kafka (Async)
- **Storage:** TimescaleDB (Postgres-based time-series)
- **Monitoring:** Prometheus Client Library
