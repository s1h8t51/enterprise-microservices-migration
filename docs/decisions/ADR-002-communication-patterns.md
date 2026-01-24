# ADR 002: Communication Patterns

## Status
Accepted

## Context
In the monolith, modules called each other via simple function calls. In a distributed system, we need to balance data consistency with system availability.

## Decision
We will use a **Hybrid Communication Model**:
1.  **Synchronous (REST/HTTP):** Used for "read" operations where immediate data is required (e.g., checking a license before login).
2.  **Asynchronous (Event-Driven via RabbitMQ/Kafka):** Used for "write" operations or side effects (e.g., when a user buys a license, the Telemetry service is notified via an event).

## Consequences
* **Pros:** Improved system resilience; if the Telemetry service is down, the Licensing service can still process sales.
* **Cons:** Increased complexity in debugging distributed traces and eventual consistency.
