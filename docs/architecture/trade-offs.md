# Technical Trade-offs & Reasoning

### 1. Database per Service vs. Shared Database
* **Decision:** Database per Service.
* **Trade-off:** We gained independent scaling and schema freedom but lost the ability to perform ACID joins across domains. 
* **Mitigation:** We implemented an **Event Mesh** to keep data synchronized.

### 2. Choice of Language (Python/FastAPI)
* **Decision:** Python 3.12 with FastAPI.
* **Trade-off:** Not as fast as Go or Rust for raw compute.
* **Reasoning:** The development velocity and the rich ecosystem for data processing (needed for the Telemetry service) outweighed the raw execution speed.

### 3. Global Consistency vs. Availability (CAP Theorem)
* **Decision:** Prioritized **Availability** (AP).
* **Reasoning:** It is better for a user to see a slightly cached entitlement than to have the entire login flow fail because a database was locked.
