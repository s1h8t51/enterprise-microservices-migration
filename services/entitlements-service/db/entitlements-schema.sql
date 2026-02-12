-- SCHEMA: entitlements_db
-- Refined to match the "Feature Storage" and "High Performance" requirements

CREATE TABLE user_entitlements (
    user_id       VARCHAR(255) PRIMARY KEY, -- Source of truth for identity
    tier_name     VARCHAR(50) NOT NULL,    -- e.g., 'enterprise', 'pro' (Synced from Licensing)
    
    -- Optimized JSONB for feature flags as per tech stack requirements
    -- Allows O(1) lookup of specific capabilities without complex joins
    -- Example: {"api_limit": 5000, "sso_enabled": true}
    features      JSONB NOT NULL DEFAULT '{}',
    
    status        VARCHAR(20) DEFAULT 'active',
    last_synced   TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- GIN index allows fast searching within the JSONB feature set
CREATE INDEX idx_entitlements_features ON user_entitlements USING GIN (features);

-- Note on Architecture:
-- 1. NO JOINS: This service never joins with Licensing. 
-- 2. ASYNC SYNC: When Licensing broadcasts SUBSCRIPTION_UPDATED via RabbitMQ,
--    this service consumes that event and updates the JSONB block here.
-- 3. LATENCY: By having all data here in JSONB, the API provides <10ms lookups.
