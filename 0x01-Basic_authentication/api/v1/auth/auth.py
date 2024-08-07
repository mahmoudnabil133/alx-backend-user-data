#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        "check if auth is required or not"
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if not request or not request.headers.get('Authorization', None):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        "current user"
        return None
