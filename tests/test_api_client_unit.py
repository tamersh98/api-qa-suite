from utils.api_client import APIClient


def test_api_client_sets_default_reqres_api_key_header(monkeypatch):
    monkeypatch.delenv("REQRES_API_KEY", raising=False)
    client = APIClient()
    assert client.session.headers["x-api-key"] == "reqres-free-v1"


def test_api_client_uses_env_reqres_api_key_header(monkeypatch):
    monkeypatch.setenv("REQRES_API_KEY", "custom-key")
    client = APIClient()
    assert client.session.headers["x-api-key"] == "custom-key"
