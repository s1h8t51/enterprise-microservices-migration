from fastapi.testclient import TestClient
from example_code.access_control_middleware import app

client = TestClient(app)

def test_validate_token_missing():
    """Tests that a request without a token is rejected."""
    # Sending a POST to validate without the Bearer header
    response = client.post("/v1/validate")
    assert response.status_code == 401

def test_get_roles_success():
    """Tests retrieving roles for a known user."""
    response = client.get("/v1/roles/user_1")
    assert response.status_code == 200
    # Ensuring the response is a list or contains role data
    assert isinstance(response.json(), (list, dict))
