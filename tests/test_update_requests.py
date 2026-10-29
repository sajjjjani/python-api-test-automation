
import requests


def test_update_post_with_put(base_url):
    payload = {
        "id": 1,
        "title": "Updated API test title",
        "body": "Updated post body using PUT",
        "userId": 1,
    }

    response = requests.put(
        f"{base_url}/posts/1",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_update_post_title_with_patch(base_url):
    payload = {
        "title": "Updated title using PATCH",
    }

    response = requests.patch(
        f"{base_url}/posts/1",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
