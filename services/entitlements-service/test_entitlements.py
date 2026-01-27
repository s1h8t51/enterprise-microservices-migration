from fastapi.testclient import TestClient
from example_code.entitlements_controller import app

client = TestClient(app)

def test_read_entitlements_success():
    # Testing our migrated endpoint
    response = client.get("/v1/users/user_1/features")
    assert response.status_code == 200
    assert response.json()["user_id"] == "user_1"

def test_read_entitlements_not_found():
    # Testing our error handling
    response = client.get("/v1/users/non_existent_user/features")
    assert response.status_code == 404
