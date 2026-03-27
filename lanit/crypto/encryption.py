import hashlib
import base64
from cryptography.fernet import Fernet

_cipher = None  # global cipher instance


def derive_key(password: str) -> bytes:
    """Derive a Fernet-compatible key from password"""
    hash_bytes = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash_bytes)


def init_cipher(password: str):
    """Initialize cipher with password"""
    global _cipher
    key = derive_key(password)
    _cipher = Fernet(key)


def encrypt(data: bytes) -> bytes:
    return _cipher.encrypt(data)


def decrypt(data: bytes) -> bytes:
    return _cipher.decrypt(data)