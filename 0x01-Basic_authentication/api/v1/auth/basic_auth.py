#!/usr/bin/env python3
"""
Basic Auth module
"""

from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import base64
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        "return value afterBasic"
        if not authorization_header or type(authorization_header) != str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        "return decoded value"
        if not base64_authorization_header:
            if type(base64_authorization_header) != str:
                return None
        try:
            return base64.b64decode(base64_authorization_header.
                                    encode('utf-8')).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        "return user credentials"
        if not decoded_base64_authorization_header:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        name, password = None, None
        for i in range(len(decoded_base64_authorization_header)):
            if decoded_base64_authorization_header[i] == ':':
                name = decoded_base64_authorization_header[:i]
                password = decoded_base64_authorization_header[i+1:]
                print(name, password)
                break

        return name, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        "return user object from username and pass"
        if not user_email or type(user_email) != str:
            return None
        if not user_pwd or type(user_pwd) != str:
            return None
        user = {'email': user_email}
        try:
            u = User.search(user)
        except Exception:
            return None

        if not u:
            return None
        u = u[0]
        if u.is_valid_password(user_pwd):
            return u
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        "return current user"
        header = self.authorization_header(request)
        en_credetionals = self.extract_base64_authorization_header(header)
        de_creditionals = self.decode_base64_authorization_header(
            en_credetionals)
        username, password = self.extract_user_credentials(de_creditionals)
        return self.user_object_from_credentials(username, password)
