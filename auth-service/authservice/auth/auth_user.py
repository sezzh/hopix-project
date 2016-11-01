from flask import jsonify
from authservice.superusers.models import Superusers
from datetime import timedelta, datetime
from authservice.lib import jwt
from authservice import encrypt


def auth_superuser(p_username, p_password):
    try:
        user = Superusers.query.filter_by(username=p_username).first()
        if user is None:
            resp = jsonify(
                    {"mensaje": "¡La usuario y/o la" +
                        " contraseña son incorectos!"}
                    )
            resp.status_code = 404
        else:
            username = user.username
            hash_encrypt = user.password
            validate = encrypt.check_sha512(p_password, hash_encrypt)
            if validate and (username == p_username):
                expire = (
                    datetime.utcnow() +
                    timedelta(minutes=1)
                    )
                token = {
                    "type": "superuser",
                    "sub": user.username,
                    'exp': expire,
                    "id": user.id,
                    "email": user.email,
                    "is_active": user.is_active
                }
                results = jwt.encode_token(token)
                resp = jsonify(
                    {"token": results, "mensaje": "Este token expira en 1 min"}
                    )
                resp.status_code = 201
            else:
                resp = jsonify(
                    {"mensaje": "¡La usuario y/o la " +
                        "contraseña son incorectos!"}
                    )
                resp.status_code = 404
            return resp
        return resp

    except Exception as e:
        resp = jsonify({"mensaje": " ¡ No tenemos conexión a la BD :( !"})
        resp.status_code = 500
        return resp
