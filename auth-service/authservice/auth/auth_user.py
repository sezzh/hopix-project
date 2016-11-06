# -*- encoding: utf-8 -*-
from flask import jsonify
from authservice.superusers.models import Superusers
from authservice.users.models import Users
from datetime import timedelta, datetime
from authservice.lib import jwt
from authservice.lib.encrypt import check_sha512
from authservice.lib.errors import error_409, error_410, error_500


def auth_superuser(req_username, req_password, req_exp):
    try:
        expiration = req_exp if req_exp is not None else 10080
        expiration = expiration if expiration < 11000 else 10080
        user = Superusers.query.filter_by(username=req_username).first()
        if user is None:
            res = error_410()
        else:
            username = user.username
            hash_encrypt = user.password
            validate = check_sha512(req_password, hash_encrypt)
            if validate and (username == req_username):
                expire = (
                    datetime.utcnow() + timedelta(minutes=expiration)
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
                res = jsonify({"token": results})
                res.status_code = 201
            else:
                err = ({
                    "sub": ["Dato incorrecto"],
                    "password": ["Dato incorrecto."]
                })
                res = error_409(err)
            return res
        return res

    except Exception as e:
        return error_500()


def auth_user(req_email, req_password, req_exp):
    try:
        expiration = req_exp if req_exp is not None else 10080
        expiration = expiration if expiration < 11000 else 10080
        user = Users.query.filter_by(email=req_email).first()
        if user is None:
            res = error_410()
        else:
            email = user.email
            hash_encrypt = user.password
            validate = check_sha512(req_password, hash_encrypt)
            if validate and (req_email == email):
                expire = (
                    datetime.utcnow() + timedelta(minutes=expiration)
                )
                token = {
                    "type": "user",
                    "sub": user.email,
                    'exp': expire,
                    "id": user.id,
                    "email": user.email,
                    "is_active": user.is_active
                }
                results = jwt.encode_token(token)
                res = jsonify({"token": results})
                res.status_code = 201
            else:
                err = ({
                    "sub": ["Dato incorrecto"],
                    "password": ["Dato incorrecto."]
                })
                res = error_409(err)
            return res
        return res

    except Exception as e:
        return error_500()
