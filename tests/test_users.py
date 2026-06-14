import pytest
from unittest.mock import patch
from utils.api_client import APIClient


def test_get_all_users_returns_200(api_client, mock_users_response):
    with patch.object(api_client.session, "request", return_value=mock_users_response):
        response = api_client.get_users()
    assert response.status_code == 200


def test_get_all_users_returns_list(api_client, mock_users_response):
    with patch.object(api_client.session, "request", return_value=mock_users_response):
        response = api_client.get_users()
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_all_users_schema(api_client, mock_users_response):
    with patch.object(api_client.session, "request", return_value=mock_users_response):
        response = api_client.get_users()
    required_keys = ["id", "name", "email", "username"]
    for user in response.json():
        for key in required_keys:
            assert key in user, f"Missing key '{key}' in user: {user}"


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_user_returns_200(api_client, mock_single_user_response, user_id):
    with patch.object(api_client.session, "request", return_value=mock_single_user_response):
        response = api_client.get_single_user(user_id)
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_user_has_correct_fields(api_client, mock_single_user_response, user_id):
    with patch.object(api_client.session, "request", return_value=mock_single_user_response):
        response = api_client.get_single_user(user_id)
    user = response.json()
    assert "id" in user
    assert "email" in user


def test_get_single_user_not_found(api_client, mock_not_found_response):
    with patch.object(api_client.session, "request", return_value=mock_not_found_response):
        response = api_client.get_single_user(9999)
    assert response.status_code == 404


def test_create_user_returns_201(api_client, mock_create_user_response):
    payload = {"name": "Test User", "email": "test@test.com", "username": "testuser"}
    with patch.object(api_client.session, "request", return_value=mock_create_user_response):
        response = api_client.create_user(payload)
    assert response.status_code == 201


def test_create_user_returns_new_id(api_client, mock_create_user_response):
    payload = {"name": "Test User", "email": "test@test.com", "username": "testuser"}
    with patch.object(api_client.session, "request", return_value=mock_create_user_response):
        response = api_client.create_user(payload)
    data = response.json()
    assert "id" in data
    assert data["id"] is not None

def test_user_has_phone_field(api_client, mock_single_user_response):
    with patch.object(api_client.session, "request", return_value=mock_single_user_response):
        response = api_client.get_single_user(1)
    assert "phone" in response.json()