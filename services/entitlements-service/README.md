# Entitlements Service

## Purpose
This service acts as the source of truth for user feature access. It decouples "Who is the user?" (Identity) from "What can they do?" (Entitlement).

## Core Responsibilities
- Provide a high-performance lookup for user feature flags.
- Sync with the **Licensing Service** via events to update user tiers.
- Cache entitlement data to minimize database load during peak traffic.

## Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL (Optimized for JSONB feature storage)
- **Caching:** Redis
