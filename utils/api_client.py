import os
import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://reqres.in/api"
        self.session = requests.Session()
        # Keep it clean so standard payload formatting works automatically
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": os.getenv("REQRES_API_KEY", "reqres-free-v1")
        })

    def get_products(self):
        """Fetches resource/product lists."""
        return self.session.get(f"{self.base_url}/unknown")

    def login(self, credentials):
        """Sends a login payload to generate a token."""
        return self.session.post(f"{self.base_url}/login", json=credentials)

    def get_users(self):
        """Fetches pages of users."""
        return self.session.get(f"{self.base_url}/users?page=1")

    def get_single_user(self, user_id):
        """Fetches a single user profile."""
        return self.session.get(f"{self.base_url}/users/{user_id}")
