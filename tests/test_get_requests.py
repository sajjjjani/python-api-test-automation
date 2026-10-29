
import requests
import pytest


def test_get_single_post(base_url):
    response = requests.get(
        f"{base_url}/posts/1",
        timeout=10,
    )

    assert response.status_code == 200

    data = response.json()

    assert set(data.keys()) == {"userId", "id", "title", "body"}
    assert data["id"] == 1
    assert isinstance(data["userId"], int)
    assert data["userId"] > 0
    assert isinstance(data["title"], str)
    assert data["title"]
    assert isinstance(data["body"], str)
    assert data["body"]


def test_get_nonexistent_post(base_url):
    response = requests.get(f"{base_url}/posts/9999", timeout=10)

    assert response.status_code == 404


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_multiple_posts(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == post_id
    assert isinstance(data["title"], str)
    assert data["title"].strip() != ""
