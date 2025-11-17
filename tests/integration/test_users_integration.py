
from fastapi import status

def test_create_user(client):
    response = client.post("/users/", json={
        "username": "user1",
        "email": "user1@example.com",
        "password": "supersecret"
    })
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == "user1"
    assert data["email"] == "user1@example.com"
    assert "id" in data
    assert "created_at" in data

def test_unique_username(client):
    # First user
    client.post("/users/", json={
        "username": "same",
        "email": "a@a.com",
        "password": "aaaaaaaA1"
    })
    # Duplicate username
    response = client.post("/users/", json={
        "username": "same",
        "email": "b@b.com",
        "password": "aaaaaaaA1"
    })
    assert response.status_code == 400 or response.status_code == 409

def test_create_user_invalid_password(client):
    response = client.post("/users/", json={
        "username": "shortpass",
        "email": "shortpass@example.com",
        "password": "123"
    })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

