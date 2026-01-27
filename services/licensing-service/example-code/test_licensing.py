from fastapi.testclient import TestClient
from services.licensing_service.example_code.license_validator import app
client = TestClient(app)
def test_health():
    assert client.get("/v1/validate?license_key=PRO-123").status_code in [200, 404]
