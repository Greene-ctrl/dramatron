from fastapi.testclient import TestClient
from dramatron.api.main import app

client = TestClient(app)

def test_get_prefixes():
    response = client.get("/prefixes")
    assert response.status_code == 200
    assert "medea_prefixes" in response.json()

# Full generation test would require a mock LLM or a real API key.
# I'll add a simple test for the endpoint structure.
def test_generate_invalid_prefix():
    response = client.post("/generate", json={
        "logline": "test",
        "prefix_set": "invalid",
        "model_provider": "google",
        "api_key": "test"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid prefix set"
