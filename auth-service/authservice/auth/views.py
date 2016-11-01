from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api, reqparse
from authservice.auth.auth_user import auth_superuser
from marshmallow import ValidationError


tokens = Blueprint('tokens', __name__)

api = Api(tokens)

parser = reqparse.RequestParser()
parser.add_argument('type', required=True,
                    help="el atributo [type] no puede estar vacío!")
parser.add_argument('sub', required=True,
                    help="el atributo [sub] no puede estar vacío!")
parser.add_argument('password', required=True,
                    help="El atributo [password] no puede estar vacío!")


class Tokens(Resource):
    def post(self):
        if request.content_type != "application/json":
            resp = jsonify({"error": "¡ Petición solicitada no soportada! :("})
            resp.status_code = 405
            return resp
        else:
            p_raw_dict = request.get_json(force=True)
            args = parser.parse_args()
            try:
                p_type = p_raw_dict['type']
                p_username = p_raw_dict['sub']
                p_password = p_raw_dict['password']
                if p_type == "superuser":
                    return auth_superuser(p_username, p_password)
                else:
                    return jsonify({"aviso": "token no soportado aún :("})

            except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 400
                return resp


api.add_resource(Tokens, '')
