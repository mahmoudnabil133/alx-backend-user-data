#!/usr/bin/env python3
"""
encrypt password module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    "hash function"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
