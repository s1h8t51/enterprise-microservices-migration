from fastapi.testclient import TestClient
from example_code.metrics_collector import app

client = TestClient(app)

def test_post_event():
    """Tests the ingestion of a telemetry event."""
    payload = {
        "service_name": "entitlements-service",
        "event_type": "login",
        "payload": {"browser": "chrome"},
        "timestamp": "2026-01-27T12:00:00Z"
    }
    response = client.post("/v1/events", json=payload)
    # Your OpenAPI spec said this returns 202 Accepted
    assert response.status_code == 202
