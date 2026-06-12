# utils/api_client.py
import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://fakestoreapi.com"

    def login(self, credentials):
        """Sends a POST request to authenticate a user."""
        return requests.post(f"{self.base_url}/auth/login", json=credentials)

    def get_users(self):
        """Fetches all registered users."""
        return requests.get(f"{self.base_url}/users")

    def get_single_user(self, user_id):
        """Fetches a single user profile by their unique ID."""
        return requests.get(f"{self.base_url}/users/{user_id}")
