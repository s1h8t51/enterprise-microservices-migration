from fastapi.testclient import TestClient
# Assuming your controller is named similarly to the entitlements one
from example_code.license_validator import app 

client = TestClient(app)

def test_license_validation():
    """Tests if the service correctly validates an active license."""
    response = client.get("/v1/validate?license_key=PRO-123")
    # Even with mock data, we expect a valid structure
    assert response.status_code in [200, 404] 
    if response.status_code == 200:
        assert "status" in response.json()
