from flask import Blueprint, request, jsonify
from authservice.superusers.models import Superusers
from flask_restful import Resource, Api
from marshmallow import ValidationError
from authservice import encrypt
from authservice.lib import jwt
from datetime import timedelta, datetime

tokens = Blueprint('tokens', __name__)

api = Api(tokens)


class Tokens(Resource):
    def post(self):
        p_raw_dict = request.get_json(force=True)
        try:
            p_name = p_raw_dict['sub']
            p_password = p_raw_dict['password']
            user = Superusers.query.filter_by(name=p_name).first()
            if user is None:
                resp = jsonify(
                    {"error": "¡El usuario y/o contraseña son incorectos!"}
                    )
                resp.status_code = 404
            else:
                name = user.name
                hash_encrypt = user.password
                validate = encrypt.check_sha512(p_password, hash_encrypt)
                if validate and (name == p_name):
                    expire = (
                        datetime.utcnow() +
                        timedelta(days=1460)
                        )
                    token = {
                        "sub": user.name,
                        'exp': expire,
                        "id": user.id,
                        "email": user.email,
                        "is_active": user.is_active
                    }
                    results = jwt.encode_token(token)
                    resp = jsonify({"token": results})
                    resp.status_code = 201
                else:
                    resp = jsonify(
                        {"error": "¡El usuario y/o contraseña son incorectos!"}
                        )
                    resp.status_code = 403
            return resp

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp

api.add_resource(Tokens, '')
