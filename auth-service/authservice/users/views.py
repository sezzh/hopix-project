# -*- encoding: utf-8 -*-
from flask import Blueprint, request, jsonify
from authservice.users.models import Users, UsersSchema, db
from flask_restful import Api, Resource

from authservice.lib.encrypt import encrypt_sha512
from authservice.lib.regex_validators import validate_password


users = Blueprint('users', __name__)
schema = UsersSchema()
api = Api(users)


# Recurso de los Users

class UsersList(Resource):
    def get(self):
        try:
            users_query = Users.query.all()
            # Serialize the queryset
            resp = schema.dump(users_query, many=True).data
            return resp
        except Exception as e:
            resp = jsonify({"mensaje": "¡ No tenemos conexión a la BD :(!"})
            resp.status_code = 500
            return resp

    def post(self):
        if request.content_type != "application/json":
            resp = jsonify({"error": "¡Petición solicitada no soportada :(!"})
            resp.status_code = 422
            return resp
        else:
            json_data = request.get_json()
            if not json_data:
                resp = jsonify({'mensaje': 'No se han proporcionado datos'})
                resp.status_code = 422
                return resp
            # validate and deserialize input
            data, errors = schema.load(json_data)
            if errors:
                return errors, 422
            try:
                email, password = data['email'], data['password']
                user = Users.query.filter_by(email=email).first()
                pw_validate = validate_password(password)
                if not pw_validate:
                    error = jsonify({"mensaje": "La contraseña es incorrecta"})
                    error.status_code = 422
                    return error

                if user is None:
                    # Create a new user
                    password_sha = encrypt_sha512(password, 10000, 10)
                    user = Users(
                        email=email,
                        password=password_sha
                    )
                    user.add(user)
                    query = Users.query.get(user.id)
                    resp = schema.dump(query).data
                    return resp, 201
                else:
                    resp = jsonify({'mensaje': 'El usuario ya existe'})
                    resp.status_code = 409
                    return resp

            except Exception as e:
                resp = jsonify({"mensaje": "¡No tenemos conexión a la BD :(!"})
                resp.status_code = 500
                return resp


api.add_resource(UsersList, '')
