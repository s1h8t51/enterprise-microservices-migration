-- SCHEMA: telemetry_db (TimescaleDB)
-- OWNED BY: telemetry-service
-- DESCRIPTION: Time-series storage for system-wide metrics and events.

-- 1. Raw Events Table (High Volume Ingestion)
CREATE TABLE telemetry_events (
    time        TIMESTAMPTZ       NOT NULL,
    event_id    UUID              NOT NULL DEFAULT gen_random_uuid(),
    service_id  VARCHAR(50)       NOT NULL,
    user_id     VARCHAR(255),
    event_type  VARCHAR(50)       NOT NULL, -- 'heartbeat', 'usage', 'error'
    payload     JSONB,                      -- Flexible metadata
    value       DOUBLE PRECISION            -- Numeric metric value if applicable
);

-- Convert to Hypertable for performance (TimescaleDB specific)
SELECT create_hypertable('telemetry_events', 'time');

-- 2. Aggregated Metrics (For Grafana/Prometheus Export)
CREATE TABLE hourly_metrics (
    time        TIMESTAMPTZ       NOT NULL,
    service_id  VARCHAR(50)       NOT NULL,
    metric_name VARCHAR(100)      NOT NULL,
    avg_value   DOUBLE PRECISION,
    max_value   DOUBLE PRECISION,
    count       BIGINT
);

SELECT create_hypertable('hourly_metrics', 'time');

-- 3. Indexes for fast lookup of user-specific usage
CREATE INDEX idx_telemetry_user_time ON telemetry_events (user_id, time DESC);
