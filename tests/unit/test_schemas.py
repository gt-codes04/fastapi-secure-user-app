from app.schemas import UserBase, UserCreate, UserRead
from datetime import datetime
import pytest


def test_user_base_fields():
    user = UserBase(username="testuser", email="test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_user_create_inherits_user_base():
    user = UserCreate(username="testuser", email="test@example.com", password="supersecret123")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password == "supersecret123"


def test_user_read_inherits_user_base():
    now = datetime.utcnow()
    user = UserRead(id=1, username="testuser", email="test@example.com", created_at=now)
    assert user.id == 1
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.created_at == now
