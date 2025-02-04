"""This module contains the security functions for the application."""

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import jwt
from datetime import datetime, timedelta
from app.core.settings import get_settings

ph = PasswordHasher()
settings = get_settings()

HASHING_ALGORITHM = "HS256"


def hash_password(raw: str) -> str:
    """This function hashes a password

    Args:
        raw (str): The raw password

    Returns:
        str: The hashed password
    """
    return ph.hash(raw)


def verify_password(plain_password: str, hashed_password: str):
    """This function verifies a password

    Args:
        plain_password (str): The plain password
        hashed_password (str): The hashed password

    Returns:
        bool: True if the password is correct, False otherwise
    """
    try:
        return ph.verify(hash=str(hashed_password), password=plain_password)
    except VerifyMismatchError:
        return False


def create_access_token(
        data: dict,
        expires_delta: timedelta = timedelta(minutes=60),
):
    """This function creates a JWT token

    Args:
        data (dict): The data to be encoded

    Returns:
        str: The JWT token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=HASHING_ALGORITHM) # noqa
