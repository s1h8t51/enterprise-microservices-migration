from fastapi.testclient import TestClient
from services.entitlements_service.example_code.entitlements_controller import app
client = TestClient(app)
def test_health():
    assert client.get("/v1/users/user_1/features").status_code == 200
