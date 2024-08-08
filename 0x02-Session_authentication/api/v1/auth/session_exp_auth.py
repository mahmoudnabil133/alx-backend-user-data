#!/usr/bin/env python3
"add expreration for session"
from .session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    "SessionExAuth"
    def __init__(self):
        "init"
        try:
            duration = int(getenv('SESSION_DURATION'))
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id=None):
        "create session ovarlap father method"
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        "get user id from session id"
        if not session_id:
            return None
        session_dic = self.user_id_by_session_id.get(session_id)
        if not session_id:
            return None
        created_at = session_dic.get('created_at')
        if not created_at:
            return None
        user_id = session_dic.get('user_id')
        if self.session_duration <= 0:
            return user_id
        window = created_at + timedelta(seconds=self.session_duration)
        if window < datetime.now():
            return None
        return user_id
