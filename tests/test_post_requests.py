
import requests


def test_create_post(base_url):
    payload = {
        "title": "API automation test",
        "body": "Testing POST requests with Pytest",
        "userId": 1,
    }

    response = requests.post(
        f"{base_url}/posts",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_create_post_with_missing_title(base_url):
    payload = {
        "body": "Post created without a title",
        "userId": 1,
    }

    response = requests.post(
        f"{base_url}/posts",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 201

    data = response.json()

    assert "title" not in data
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
