import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://fakestoreapi.com"

    def get_products(self):
        return requests.get(f"{self.base_url}/products")

    def create_product(self, payload):
        return requests.post(f"{self.base_url}/products", json=payload)
