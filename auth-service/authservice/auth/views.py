# -*- encoding: utf-8 -*-
from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse
from authservice.auth.auth_user import auth_superuser, auth_user
from marshmallow import ValidationError
from authservice.lib.errors import error_409, error_410, error_422, error_500
from authservice.auth.models import TokenSchema

tokens = Blueprint('tokens', __name__)
schema = TokenSchema()
api = Api(tokens)


class Tokens(Resource):
    def post(self):
        if request.content_type != "application/json":
            err = {"content_type": ["Se esperaba application/json"]}
            return error_422(err)
        else:
            json_data = request.get_json(force=True)
            if not json_data:
                err = {"datos": ["Información insuficientes."]}
                return error_422(err)
            data, errors = schema.load(json_data)
            req_type = data.get('type')
            req_exp = data.get('exp') if data.get('exp') is not None else 10080
            req_email = data.get('email')
            req_pw = data.get('password')

            if errors:
                return error_422(errors)
            elif req_type is None:
                return auth_user(req_email, req_pw, req_exp)
            elif req_type == "superuser":
                return auth_superuser(req_email, req_pw, req_exp)
            else:
                err = {"type": ["Tipo de autentificación no válida."]}
                return error_422(err)


api.add_resource(Tokens, '')
