from jose import jwt
from authservice.config_jwt import jwt_secret


def encode_token(claims):
    token = jwt.encode(claims, jwt_secret, algorithm='HS256')
    return token


def decode_token(token):
    payload = jwt.decode(token, jwt_secret, algorithms=['HS256'])
    return payload
