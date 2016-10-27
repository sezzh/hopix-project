from jose import jwt


def encode_token(claims):
    token = jwt.encode(claims, 'secret', algorithm='HS256')
    return token


def decode_token():
    # deco = jwt.decode(token, 'secret', algorithms=['HS256'])
    pass
