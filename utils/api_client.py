# utils/api_client.py
import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://fakestoreapi.com"
        # Create a persistent session and append a generic browser User-Agent
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def get_products(self):
        """Fetches all inventory products."""
        return self.session.get(f"{self.base_url}/products")

    def login(self, credentials):
        """Sends a POST request to authenticate a user."""
        return self.session.post(f"{self.base_url}/auth/login", json=credentials)

    def get_users(self):
        """Fetches all registered users."""
        return self.session.get(f"{self.base_url}/users")

    def get_single_user(self, user_id):
        """Fetches a single user profile by their unique ID."""
        return self.session.get(f"{self.base_url}/users/{user_id}")
