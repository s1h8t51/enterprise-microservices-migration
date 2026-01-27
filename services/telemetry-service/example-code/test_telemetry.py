from fastapi.testclient import TestClient
from services.telemetry_service.example_code.metrics_collector import app
client = TestClient(app)
def test_health():
    payload = {"service_name": "test", "event_type": "check", "payload": {}, "timestamp": "2026-01-27T12:00:00Z"}
    assert client.post("/v1/events", json=payload).status_code == 202
