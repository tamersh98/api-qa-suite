import pytest
from unittest.mock import patch
from utils.api_client import APIClient


def test_get_all_products_returns_200(api_client, mock_posts_response):
    with patch.object(api_client.session, "request", return_value=mock_posts_response):
        response = api_client.get_products()
    assert response.status_code == 200


def test_get_all_products_returns_list(api_client, mock_posts_response):
    with patch.object(api_client.session, "request", return_value=mock_posts_response):
        response = api_client.get_products()
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_all_products_schema(api_client, mock_posts_response):
    with patch.object(api_client.session, "request", return_value=mock_posts_response):
        response = api_client.get_products()
    required_keys = ["id", "userId", "title", "body"]
    for product in response.json():
        for key in required_keys:
            assert key in product, f"Missing key '{key}' in product: {product}"


def test_get_single_product_returns_200(api_client, mock_single_post_response):
    with patch.object(api_client.session, "request", return_value=mock_single_post_response):
        response = api_client.get_single_product(1)
    assert response.status_code == 200


def test_get_single_product_not_found(api_client, mock_not_found_response):
    with patch.object(api_client.session, "request", return_value=mock_not_found_response):
        response = api_client.get_single_product(9999)
    assert response.status_code == 404


def test_api_performance_sla(api_client, mock_posts_response):
    with patch.object(api_client.session, "request", return_value=mock_posts_response):
        response = api_client.get_products()
    assert response.elapsed.total_seconds() < 1.0
