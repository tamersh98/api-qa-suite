import pytest
from unittest.mock import patch, MagicMock
from utils.api_client import APIClient


def test_api_client_uses_default_base_url(monkeypatch):
    monkeypatch.delenv("API_BASE_URL", raising=False)
    client = APIClient()
    assert client.base_url == "https://jsonplaceholder.typicode.com"


def test_api_client_uses_env_base_url(monkeypatch):
    monkeypatch.setenv("API_BASE_URL", "https://my-mock-server.local")
    client = APIClient()
    assert client.base_url == "https://my-mock-server.local"


def test_api_client_uses_constructor_base_url():
    client = APIClient(base_url="https://custom.api.local")
    assert client.base_url == "https://custom.api.local"


def test_api_client_sets_json_headers():
    client = APIClient()
    assert client.session.headers["Accept"] == "application/json"
    assert client.session.headers["Content-Type"] == "application/json"


def test_get_users_calls_correct_endpoint(monkeypatch):
    client = APIClient()
    mock_resp = MagicMock()
    mock_resp.status_code = 200

    with patch.object(client.session, "request", return_value=mock_resp) as mock_req:
        client.get_users()
        mock_req.assert_called_once_with("GET", "https://jsonplaceholder.typicode.com/users")


def test_get_single_user_calls_correct_endpoint():
    client = APIClient()
    mock_resp = MagicMock()
    mock_resp.status_code = 200

    with patch.object(client.session, "request", return_value=mock_resp) as mock_req:
        client.get_single_user(42)
        mock_req.assert_called_once_with("GET", "https://jsonplaceholder.typicode.com/users/42")


def test_create_user_sends_post_with_payload():
    client = APIClient()
    mock_resp = MagicMock()
    mock_resp.status_code = 201
    payload = {"name": "Alice", "email": "alice@example.com"}

    with patch.object(client.session, "request", return_value=mock_resp) as mock_req:
        client.create_user(payload)
        mock_req.assert_called_once_with(
            "POST", "https://jsonplaceholder.typicode.com/users", json=payload
        )


def test_get_products_calls_correct_endpoint():
    client = APIClient()
    mock_resp = MagicMock()
    mock_resp.status_code = 200

    with patch.object(client.session, "request", return_value=mock_resp) as mock_req:
        client.get_products()
        mock_req.assert_called_once_with("GET", "https://jsonplaceholder.typicode.com/posts")
