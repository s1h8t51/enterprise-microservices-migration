from fastapi.testclient import TestClient
from services.access_control_service.example_code.access_control_middleware import app
client = TestClient(app)
def test_health():
    assert client.post("/v1/validate").status_code == 401
