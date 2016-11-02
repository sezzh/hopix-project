# -*- encoding: utf-8 -*-
from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, reqparse
from authservice.auth.auth_user import auth_superuser, auth_user
from marshmallow import ValidationError


tokens = Blueprint('tokens', __name__)

api = Api(tokens)

parser = reqparse.RequestParser()

parser.add_argument('type', required=False, type=str,
                    help="el atributo [type] no puede estar vacío!"
                    )

parser.add_argument('sub', required=True, type=str,
                    help="el atributo [sub] no puede estar vacío!"
                    )

parser.add_argument('password', required=True, type=str,
                    help="El atributo [password] no puede estar vacío!"
                    )

parser.add_argument('exp', required=False, type=int)


class Tokens(Resource):
    def post(self):
        if request.content_type != "application/json":
            resp = jsonify({"error": "¡ Petición solicitada no soportada! :("})
            resp.status_code = 422
            return resp
        else:
            args = parser.parse_args()
            p_type = args.type if args.type is not None else "user"
            try:
                if p_type == "superuser":
                    return auth_superuser(args.sub, args.password, args.exp)
                elif p_type == "user":
                    return auth_user(args.sub, args.password, args.exp)
                else:
                    resp = jsonify({"aviso": "token no soportado aún :("})
                    resp.status_code = 422
                    return resp

            except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 422
                return resp


api.add_resource(Tokens, '')
