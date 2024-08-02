#!/usr/bin/env python3
"""
Main -1 file
"""

# hash_password = __import__('encrypt_password').hash_password

# password = "MyAmazingPassw0rd"
# print(hash_password(password))

"""
Main -2 file
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))
