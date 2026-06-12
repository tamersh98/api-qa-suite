import os
import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://reqres.in/api"
        self.session = requests.Session()
        self._api_key_candidates = self._build_api_key_candidates()
        # Keep it clean so standard payload formatting works automatically
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        if self._api_key_candidates:
            self.session.headers["x-api-key"] = self._api_key_candidates[0]

    def _build_api_key_candidates(self):
        candidates = []
        configured_key = os.getenv("REQRES_API_KEY")
        if configured_key:
            candidates.append(configured_key)
        for key in ("reqres-free-v1", "reqres-free-v2"):
            if key not in candidates:
                candidates.append(key)
        return candidates

    def _request(self, method, path, **kwargs):
        response = None
        for key in self._api_key_candidates:
            self.session.headers["x-api-key"] = key
            response = self.session.request(method, f"{self.base_url}{path}", **kwargs)
            if response.status_code not in (401, 403):
                return response
        return response

    def get_products(self):
        """Fetches resource/product lists."""
        return self._request("GET", "/unknown")

    def login(self, credentials):
        """Sends a login payload to generate a token."""
        return self._request("POST", "/login", json=credentials)

    def get_users(self):
        """Fetches pages of users."""
        return self._request("GET", "/users?page=1")

    def get_single_user(self, user_id):
        """Fetches a single user profile."""
        return self._request("GET", f"/users/{user_id}")
