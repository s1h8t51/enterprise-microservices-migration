-- Licensing Service Schema
-- Owns license keys and activation data

CREATE TABLE licenses (
    license_id UUID PRIMARY KEY,
    license_key VARCHAR(255) UNIQUE NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    customer_id VARCHAR(255) NOT NULL,
    activation_status VARCHAR(50) DEFAULT 'pending',
    max_activations INT DEFAULT 1,
    current_activations INT DEFAULT 0,
    issued_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_licenses_key ON licenses(license_key);
CREATE INDEX idx_licenses_customer ON licenses(customer_id);
CREATE INDEX idx_licenses_status ON licenses(activation_status);

-- This service exposes /api/licenses/validate endpoint
-- Other services call this API, they DON'T query this table directly
