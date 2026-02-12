-- Entitlements Service Schema
-- Owns user access grants and permissions

CREATE TABLE user_entitlements (
    entitlement_id UUID PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    access_level VARCHAR(50) NOT NULL,
    granted_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_user_entitlements_user ON user_entitlements(user_id);
CREATE INDEX idx_user_entitlements_product ON user_entitlements(product_id);
CREATE INDEX idx_user_entitlements_status ON user_entitlements(status);

-- Entitlements are NEVER joined with Licensing tables
-- License validation happens via API call to Licensing service
