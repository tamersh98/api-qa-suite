# tests/test_products.py
import pytest
from utils.api_client import APIClient

# Initialize the client locally if not using a shared fixture setup
client = APIClient()

def test_get_all_products_returns_200():
    response = client.get_products()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_api_performance_sla():
    response = client.get_products()
    # Performance assertion: ensuring response SLA latency is met
    assert response.elapsed.total_seconds() < 1.0
