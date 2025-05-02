import pytest
from fastapi.testclient import TestClient
from backend.app import app
from backend.utils.security import generate_token

client = TestClient(app)

def test_search_media_with_keyword_and_db_filter():
    payload = {
        "keyword": "funeral",
        "db_filter": ["st", "sp"]
    }
    response = client.post("/search", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)

def test_search_media_with_empty_filter():
    payload = {
        "keyword": "funeral",
        "db_filter": []
    }
    response = client.post("/search", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)

def test_search_media_with_no_keyword():
    payload = {
        "keyword": "",
        "db_filter": ["st"]
    }
    response = client.post("/search", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data

def test_valid_thumbnail_redirect():
    token = generate_token("stock", "123456789")
    response = client.get(f"/thumbnail/{token}", follow_redirects=False)
    assert response.status_code == 307  # Temporary Redirect
    assert response.headers["location"].endswith("/stock/0123456789/s.jpg")

def test_invalid_token():
    invalid_token = "invalidtoken"
    response = client.get(f"/thumbnail/{invalid_token}")
    assert response.status_code == 403
    assert response.json()["detail"] == "Invalid token"