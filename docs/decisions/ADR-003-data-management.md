# ADR 003: Data Management Strategy

## Status
Accepted

## Context
The legacy system used a single, massive SQL database with 400+ tables. This created a "distributed monolith" risk where services are coupled at the database level.

## Decision
We will adopt the **Database-per-Service** pattern.
* **Entitlements:** Relational (PostgreSQL) for complex permission queries.
* **Telemetry:** Time-series optimized (TimescaleDB or InfluxDB).
* **Licensing:** High-audit Relational (PostgreSQL) with Row-Level Security.

**Data Consistency:** We will use the **Saga Pattern (Choreography-based)** to manage distributed transactions rather than 2-Phase Commits (2PC).

## Consequences
* **Pros:** Each service can scale its storage independently; no single point of failure for data.
* **Cons:** Cross-service reporting becomes difficult; requires an ETL process or Data Lake for "Big Picture" analytics.
