import pytest
from fastapi import status

def test_create_user(client):
    response = client.post("/users/", json={
        "username": "integrationuser",
        "email": "integration@example.com",
        "password": "integrationpass123"
    })
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["username"] == "integrationuser"
    assert data["email"] == "integration@example.com"
    assert "id" in data
    assert "created_at" in data

def test_create_user_duplicate_username(client):
    # First user
    client.post("/users/", json={
        "username": "dupeuser",
        "email": "dupe1@example.com",
        "password": "dupepass123"
    })
    # Duplicate username
    response = client.post("/users/", json={
        "username": "dupeuser",
        "email": "dupe2@example.com",
        "password": "dupepass456"
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST or response.status_code == status.HTTP_409_CONFLICT

def test_create_user_invalid_password(client):
    response = client.post("/users/", json={
        "username": "shortpass",
        "email": "shortpass@example.com",
        "password": "123"
    })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
