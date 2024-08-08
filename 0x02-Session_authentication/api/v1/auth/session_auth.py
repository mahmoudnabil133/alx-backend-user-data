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
from models.user import User
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


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    "login"
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        res = jsonify(user.to_json())
        cookie_key = getenv('SESSION_NAME')
        res.set_cookie(cookie_key, session_id)
        return res
