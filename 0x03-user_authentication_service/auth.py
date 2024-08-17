#!/usr/bin/env python3
"""
authentication module
to hanle signup, login, sessions
updateing passwords to user
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    "return hashed password"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    "gen uuid"
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        "/sign up a new user"
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        "check if login is valid or not"
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
        except Exception:
            return False
        return False

    def create_session(self, email: str) -> str:
        "create session"
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        sess_id = _generate_uuid()
        self._db.update_user(user.id, session_id=sess_id)
        return sess_id

    def get_user_from_session_id(self, session_id: str) -> User:
        "get user by session_id"
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        "destroy session"
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass
        return None

    def get_reset_password_token(self, email: str) -> str:
        "get password reset token and update user in db"
        try:
            reset_token = _generate_uuid()
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        "update user with given reset Token"
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_pass = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_pass,
                                 reset_token=None)
        except Exception:
            raise ValueError
        return None
