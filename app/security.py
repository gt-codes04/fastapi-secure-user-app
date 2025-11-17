# app/security.py
from passlib.context import CryptContext

# Use Argon2 instead of bcrypt to avoid backend issues and keep strong security
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Hash a plain-text password using Argon2."""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    """Verify a plain-text password against the stored hash."""
    return pwd_context.verify(plain_password, password_hash)
