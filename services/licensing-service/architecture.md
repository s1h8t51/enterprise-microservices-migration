# Licensing Service Architecture

## Security and Integrity
Because this service handles revenue-generating data, we prioritize **Data Integrity** over throughput.

### Key Components:
1.  **The Key Master:** A dedicated module that uses a Private Key (stored in a secure Vault) to sign license data.
2.  **State Machine:** Subscriptions follow a strict state machine (Pending -> Active -> Expired -> Cancelled) to prevent illegal state transitions.
3.  **Consistency Strategy:** Uses a **Transactional Outbox Pattern**. When a license is updated, the database record and the "Update Event" are saved in the same transaction to ensure the rest of the system never misses a change.

## Integration Pattern
When a user buys a license here:
1.  **Licensing Service** saves the record.
2.  **Licensing Service** publishes a `LICENSE_ISSUED` event.
3.  **Entitlements Service** consumes the event and updates what the user sees in the UI.
