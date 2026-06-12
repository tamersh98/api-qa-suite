import pytest
from utils.api_client import APIClient

client = APIClient()

def test_get_all_products_returns_200():
    response = client.get_products()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_api_performance_sla():
    response = client.get_products()
    # Ensure response time is under 500ms
    assert response.elapsed.total_seconds() < 0.5
