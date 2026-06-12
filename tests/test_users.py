# tests/test_users.py
import pytest

def test_user_login_successful(api_client):
    credentials = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = api_client.login(credentials)
    assert response.status_code == 200
    assert "token" in response.json()

def test_user_login_invalid_credentials(api_client):
    bad_credentials = {
        "email": "missing-password@reqres.in"
    }
    response = api_client.login(bad_credentials)
    # ReqRes returns 400 Bad Request for uncompleted auth payloads
    assert response.status_code == 400

def test_get_all_users_schema(api_client, auth_token):
    assert auth_token is not None
    response = api_client.get_users()
    assert response.status_code == 200
    
    data_list = response.json().get("data", [])
    assert len(data_list) > 0
    
    first_user = data_list[0]
    required_keys = ["id", "email", "first_name", "last_name", "avatar"]
    for key in required_keys:
        assert key in first_user

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_user_parameterized(api_client, user_id):
    response = api_client.get_single_user(user_id)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id
