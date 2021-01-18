import hashlib
import os


def encrypt(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key


def verify(password, stored):
    salt = stored[:32]
    key = stored[32:]
    new_key = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 100000)
    return new_key == key
