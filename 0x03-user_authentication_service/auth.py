#!/usr/bin/env python3
"auth"

import bcrypt


def _hash_password(password: str) -> bytes:
    "return hashed password"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
