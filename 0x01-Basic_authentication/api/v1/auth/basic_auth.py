#!/usr/bin/env python3
"""
Basic Auth module
"""

from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import base64


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
