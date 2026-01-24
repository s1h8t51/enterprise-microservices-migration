# ADR 001: Defining Service Boundaries

## Status
Accepted

## Context
The legacy monolith suffers from "The Big Ball of Mud" syndrome. Code related to user licensing, feature permissions, and usage tracking is tightly coupled, making it impossible to scale one without the others. We need a logic-based approach to split these into independent services.

## Decision
We will use **Domain-Driven Design (DDD)** to identify Bounded Contexts. Each service will own its own logic and data store.

The following boundaries are established:

1.  **Entitlements Service:** Handles the mapping of users to features. (e.g., "Does User A have the 'Export' button enabled?")
2.  **Access Control Service:** Responsible for Authentication and Authorization (Identity).
3.  **Licensing Service:** Manages the legal contract—purchases, renewals, and seat counts.
4.  **Telemetry Service:** Ingests high-frequency usage data for billing and auditing.

## Criteria for Boundaries
* **Independent Scalability:** Telemetry needs to scale 10x more than Licensing.
* **Team Autonomy:** Teams should be able to deploy Entitlements without coordinating with the Licensing team.
* **Data Isolation:** Licensing data is highly sensitive (PII/Financial) and must be separated from usage logs.

## Consequences
* **Pros:** Improved fault isolation; if Telemetry goes down, users can still log in and check their licenses.
* **Cons:** Introduces "Distributed Complexity." Operations that were once a single SQL join now require an API call or event-driven synchronization.
