#!/usr/bin/env python3
"""
Session Auth module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import uuid


class SessionAuth(Auth):
    """SessionAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if not user_id or type(user_id) != str:
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
