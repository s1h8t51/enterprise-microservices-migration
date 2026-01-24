# Entitlements Service Architecture

## Design Pattern: Hexagonal (Ports and Adapters)
We use this pattern to ensure the business logic for calculating entitlements is independent of the database or the API framework.

### Components
1. **API Layer (FastAPI):** Handles HTTP requests and schema validation.
2. **Domain Logic:** Evaluates if a user's license tier permits a specific feature.
3. **Repository Layer:** Interfaces with PostgreSQL and Redis.
4. **Event Consumer:** Listens to `LICENSE_PURCHASED` events from RabbitMQ to instantly refresh the local Entitlements cache.

## Data Model
We use a **JSONB** column in Postgres to store `feature_overrides`, allowing us to enable "beta" features for specific users without a schema migration.
