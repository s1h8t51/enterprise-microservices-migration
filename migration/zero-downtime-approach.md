# Zero-Downtime Approach

Our goal was a 100% availability migration. We achieved this through three primary technical implementations:

### 1. The Strangler Fig Pattern
The monolith was never "switched off" all at once. It was slowly "strangled" by replacing its edges with microservices. This allowed us to keep the system running while replacing internal parts.

### 2. Canary Releases
We used **Progressive Delivery**. 
* **1% Traffic:** Internal testers and "Beta" users.
* **10% Traffic:** Regional rollout.
* **100% Traffic:** Global rollout.

### 3. Database Migration: Expand and Contract
To avoid downtime during schema changes:
1. **Expand:** Add new columns/tables to the DB.
2. **Migrate:** Update the code to write to both old and new structures.
3. **Contract:** Once all code is updated, remove the old columns.
