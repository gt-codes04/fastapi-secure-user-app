# app/crud.py
from sqlalchemy.orm import Session

from app import models, schemas
from app.security import hash_password


def get_user_by_username(db: Session, username: str):
    """Return a single user by username, or None if not found."""
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    """Return a single user by email, or None if not found."""
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user_in: schemas.UserCreate):
    """Create a new user with a hashed password."""
    hashed = hash_password(user_in.password)
    user = models.User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hashed,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

