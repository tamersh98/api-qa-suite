# tests/conftest.py
import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """Provides a single instance of the API client for the entire test session."""
    return APIClient()

@pytest.fixture(scope="session")
def auth_token(api_client):
    """Logs in a mock user and returns an access token for protected endpoints."""
    credentials = {
        "username": "johnd",  # Standard mock user from Fake-Store API
        "password": "m38rmF$"
    }
    
    response = api_client.login(credentials)
    
    # QA Check: Ensure authentication succeeded before running dependent tests
    assert response.status_code == 200, "Setup Failure: Could not authenticate mock user."
    
    token = response.json().get("token")
    assert token is not None, "Setup Failure: Token missing from auth response."
    
    return token
