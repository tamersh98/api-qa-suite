import pytest
from unittest.mock import patch, MagicMock
from utils.api_client import APIClient


def make_response(status_code, json_data):
    mock = MagicMock()
    mock.status_code = status_code
    mock.json.return_value = json_data
    mock.elapsed.total_seconds.return_value = 0.1
    return mock


MOCK_USERS = [
    {"id": 1, "name": "Leanne Graham", "email": "sincere@april.biz", "username": "Bret"},
    {"id": 2, "name": "Ervin Howell",  "email": "shanna@melissa.tv", "username": "Antonette"},
    {"id": 3, "name": "Clementine Bauch", "email": "nathan@yesenia.net", "username": "Samantha"},
]

MOCK_POSTS = [
    {"id": 1, "userId": 1, "title": "Post One",   "body": "Body one"},
    {"id": 2, "userId": 1, "title": "Post Two",   "body": "Body two"},
    {"id": 3, "userId": 2, "title": "Post Three", "body": "Body three"},
]


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture
def mock_users_response():
    return make_response(200, MOCK_USERS)


@pytest.fixture
def mock_single_user_response():
    return make_response(200, MOCK_USERS[0])


@pytest.fixture
def mock_posts_response():
    return make_response(200, MOCK_POSTS)


@pytest.fixture
def mock_single_post_response():
    return make_response(200, MOCK_POSTS[0])


@pytest.fixture
def mock_create_user_response():
    new_user = {"id": 11, "name": "Test User", "email": "test@test.com", "username": "testuser"}
    return make_response(201, new_user)


@pytest.fixture
def mock_not_found_response():
    return make_response(404, {"error": "Not Found"})
