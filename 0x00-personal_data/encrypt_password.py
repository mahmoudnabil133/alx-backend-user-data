#!/usr/bin/env python3
"""
encrypt password module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    "hash function"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    "check if password is same hashed one"

    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    return False
