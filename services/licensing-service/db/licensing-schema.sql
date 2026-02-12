- SCHEMA: licensing_db
-- Authoritative source for license keys, hardware binding, and contract validity.

CREATE TABLE licenses (
    license_id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    license_key      VARCHAR(255) UNIQUE NOT NULL,
    product_id       VARCHAR(255) NOT NULL,
    customer_id      VARCHAR(255) NOT NULL,
    
    -- "Entitlement Profile" - a reference used by the Entitlements service 
    -- to know which JSON feature set to apply.
    plan_tier        VARCHAR(50) NOT NULL DEFAULT 'standard', 
    
    -- Cryptographic hash or signature of the license data.
    -- Allows the Entitlements service to verify the key offline via Public Key.
    digital_signature TEXT NOT NULL,
    
    status           VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'expired', 'revoked')),
    max_activations  INT DEFAULT 1,
    
    issued_at        TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at       TIMESTAMP WITH TIME ZONE,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Activation Tracking (Decoupled to prevent locking on the 'licenses' table)
CREATE TABLE license_activations (
    activation_id    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    license_id       UUID REFERENCES licenses(license_id),
    device_fingerprint VARCHAR(255) NOT NULL, -- Hardware ID/Fingerprint
    ip_address       INET,
    activated_at     TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(license_id, device_fingerprint) -- Prevents double-activation of same device
);

-- Indexes for performance
CREATE INDEX idx_licenses_customer_lookup ON licenses(customer_id, status);
CREATE INDEX idx_licenses_expiry ON licenses(expires_at) WHERE status = 'active';

-- Multi-tenant Security (As per your tech stack)
ALTER TABLE licenses ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON licenses USING (customer_id = current_setting('app.current_customer'));
