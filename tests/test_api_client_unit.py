from utils.api_client import APIClient


def test_api_client_sets_default_reqres_api_key_header(monkeypatch):
    monkeypatch.delenv("REQRES_API_KEY", raising=False)
    client = APIClient()
    assert client.session.headers["x-api-key"] == "reqres-free-v1"


def test_api_client_uses_env_reqres_api_key_header(monkeypatch):
    monkeypatch.setenv("REQRES_API_KEY", "custom-key")
    client = APIClient()
    assert client.session.headers["x-api-key"] == "custom-key"


def test_api_client_retries_with_fallback_key_after_401(monkeypatch):
    monkeypatch.setenv("REQRES_API_KEY", "bad-key")
    client = APIClient()

    class Response:
        def __init__(self, status_code):
            self.status_code = status_code

    responses = [Response(401), Response(200)]
    used_keys = []

    def fake_request(method, url, **kwargs):
        used_keys.append(client.session.headers["x-api-key"])
        return responses.pop(0)

    monkeypatch.setattr(client.session, "request", fake_request)
    response = client.get_products()

    assert response.status_code == 200
    assert used_keys == ["bad-key", "reqres-free-v1"]
