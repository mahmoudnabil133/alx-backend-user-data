#!/usr/bin/env python3
"""
Session Auth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """SessionAuth class"""

    def create_session(self, user_id=None):
        "create session ovarlap father method"
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        kw = {
            'user_id': user_id,
            'session_id': session_id
        }
        user = UserSession(**kw)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        "get user id from session id"
        user_id = UserSession.search({"session_id": session_id})
        if not user_id:
            return None
        return user_id

    def destroy_session(self, request=None):
        """
        Destroy Session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False
