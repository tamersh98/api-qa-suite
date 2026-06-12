# tests/test_users.py
import pytest

def test_user_login_successful(api_client):
    """Positive Test: Verifies that a valid user can log in and receive a token."""
    credentials = {
        "username": "johnd",
        "password": "m38rmF$"
    }
    response = api_client.login(credentials)
    
    assert response.status_code == 200
    assert "token" in response.json()
    assert isinstance(response.json()["token"], str)

def test_user_login_invalid_credentials(api_client):
    """Negative Test: Verifies that logging in with incorrect credentials fails gracefully."""
    bad_credentials = {
        "username": "wrong_user",
        "password": "bad_password"
    }
    response = api_client.login(bad_credentials)
    
    # FakeStoreAPI returns 401 Unauthorized for bad login attempts
    assert response.status_code == 401

def test_get_all_users_schema(api_client, auth_token):
    """Data Validation Test: Verifies the schema structure of the users list."""
    # This test requires an authorized token session, passed automatically via fixture
    assert auth_token is not None 
    
    response = api_client.get_users()
    assert response.status_code == 200
    
    users = response.json()
    assert len(users) > 0
    
    # Boundary/Sanity Check on fields inside the first user object
    first_user = users[0]
    required_keys = ["id", "email", "username", "password", "name"]
    for key in required_keys:
        assert key in first_user, f"Missing required key: '{key}' in user schema data."

@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_single_user_parameterized(api_client, user_id):
    """Data-Driven Test: Validates multiple distinct user profiles using parameterization."""
    response = api_client.get_single_user(user_id)
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
