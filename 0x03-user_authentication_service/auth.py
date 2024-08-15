#!/usr/bin/python3
"auth"

import bcrypt


def _hash_password(password):
    "return hashed password"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
