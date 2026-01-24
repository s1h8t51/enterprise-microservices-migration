# Licensing Service

## Purpose
The Licensing Service manages the lifecycle of customer contracts and product subscriptions. It is the authoritative source for "What has the customer paid for?"

## Core Responsibilities
- **Subscription Management:** Handling sign-ups, renewals, and cancellations.
- **License Key Generation:** Creating signed, tamper-proof license keys.
- **Audit Logging:** Maintaining a strict history of changes for compliance and financial reporting.
- **Billing Integration:** Synchronizing with external payment processors (e.g., Stripe).

## Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL (with Row-Level Security for multi-tenancy)
- **Security:** RSA/Ed25519 for digital signatures
- **Messaging:** RabbitMQ (to broadcast `SUBSCRIPTION_UPDATED` events)
