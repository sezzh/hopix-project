from flask import Blueprint, request, jsonify
from authservice.superusers.models import Superusers, UserSchema
from flask_restful import Resource, Api
from marshmallow import ValidationError
from authservice import encrypt
from authservice.lib import jwt
tokens = Blueprint('tokens', __name__)
schema = UserSchema()
api = Api(tokens)


class Tokens(Resource):
    def post(self):
        p_raw_dict = request.get_json(force=True)
        try:
            schema.validate(p_raw_dict)
            p_superuser_dict = p_raw_dict['data']['attributes']
            p_email = p_superuser_dict['email']
            p_password = p_superuser_dict['password']
            superuser = Superusers.query.filter_by(email=p_email).first()
            if superuser is None:
                resp = jsonify({"error": "El super usuario no exite"})
                resp.status_code = 403
            else:
                email = superuser.email
                hash_encrypt = superuser.password
                validate = encrypt.check_sha512(p_password, hash_encrypt)
                if validate and (email == p_email):
                    results = schema.dump(superuser).data
                    token = jwt.encode_token(results)
                    resp = {"token": token}
                    return resp, 201
                else:
                    resp = jsonify(
                        {"error": "Email y/o Contraseña Incorectos"})
                    resp.status_code = 403
                    return resp
            return resp

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp

api.add_resource(Tokens, '.json')
