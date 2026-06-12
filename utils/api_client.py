import os
import requests


class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _request(self, method, path, **kwargs):
        return self.session.request(method, f"{self.base_url}{path}", **kwargs)

    def get_users(self):
        """Fetches list of users."""
        return self._request("GET", "/users")

    def get_single_user(self, user_id):
        """Fetches a single user by ID."""
        return self._request("GET", f"/users/{user_id}")

    def create_user(self, payload):
        """Creates a new user."""
        return self._request("POST", "/users", json=payload)

    def get_products(self):
        """Fetches list of products/posts."""
        return self._request("GET", "/posts")

    def get_single_product(self, product_id):
        """Fetches a single product by ID."""
        return self._request("GET", f"/posts/{product_id}")
