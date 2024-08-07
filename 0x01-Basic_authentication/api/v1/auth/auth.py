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
        return False
    
    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        "current user"
        return None
