#!/usr/bin/env python3
"auth"

import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    "return hashed password"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        "/sign up a new user"
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            user = None
        if user:
            raise ValueError(f"User {email} already exists")
        new_user = self._db.add_user(email, _hash_password(password))
        return new_user
