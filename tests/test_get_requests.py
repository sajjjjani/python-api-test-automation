
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"



def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    data = response.json()

    # Check the response structure
    assert set(data.keys()) == {"userId", "id", "title", "body"}

    # Check field values and data types
    assert data["id"] == 1
    assert isinstance(data["userId"], int)
    assert data["userId"] > 0
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

    # Check that text fields are not empty
    assert data["title"].strip() != ""
    assert data["body"].strip() != ""


def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/9999", timeout=10)

    assert response.status_code == 404


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_multiple_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == post_id
    assert isinstance(data["title"], str)
    assert data["title"].strip() != ""
