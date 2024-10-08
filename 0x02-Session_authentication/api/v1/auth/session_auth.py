#!/usr/bin/env python3
"""
Session Auth module
"""
from api.v1.auth.auth import Auth
from flask import request, jsonify
from typing import List, TypeVar
from models.user import User
import uuid
from api.v1.views import app_views
from os import getenv


class SessionAuth(Auth):
    """SessionAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        "create session for user"
        if not user_id or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        "get user for by session id"
        if not session_id or type(session_id) != str:
            return None
        if self.user_id_by_session_id.get(session_id, None) is None:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        "overload Auth current user"
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(str(session_id))
        cur_user = User.get(user_id)
        print(session_id, user_id, cur_user)
        return cur_user

    def destroy_session(self, request=None):
        "remove session id from memory"
        if not request:
            return False
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if not session_id or not user_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
