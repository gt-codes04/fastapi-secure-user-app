
from app.security import hash_password, verify_password

def test_hash_password_returns_different_hashes_for_same_password():
    password = "mysecretpassword"
    hash1 = hash_password(password)
    hash2 = hash_password(password)
    assert hash1 != hash2  # Hashes should be different due to salt
    assert hash1.startswith("$argon2")

def test_verify_password_success():
    password = "anothersecret"
    hashed = hash_password(password)
    assert verify_password(password, hashed)

def test_verify_password_failure():
    password = "password1"
    wrong_password = "password2"
    hashed = hash_password(password)
    assert not verify_password(wrong_password, hashed)
