from hashlib import md5
from flask import request

def hash_all(*args):
    strings = map(str, args)
    return md5(bytes(':'.join(strings), 'utf-8')).hexdigest()

def digest(hA1, hA2):
    auth = request.authorization
    return hash_all(hA1, auth.nonce, auth.nc, auth.cnonce, auth.qop, hA2)
