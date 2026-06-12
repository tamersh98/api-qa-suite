# tests/conftest.py
import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient()

@pytest.fixture(scope="session")
def auth_token(api_client):
    credentials = {
        "email": "eve.holt@reqres.in",  # Valid ReqRes mock user
        "password": "cityslicka"
    }
    response = api_client.login(credentials)
    assert response.status_code == 200, f"Setup Failure: {response.status_code}"
    return response.json().get("token")
