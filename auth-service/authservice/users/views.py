# -*- encoding: utf-8 -*-
from flask import Blueprint, request, make_response, jsonify
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
            query_set = Users.query.all()
            # Serializamos el query set indicando con many que es un array
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            # Excepción si falla la conexión
            res = make_response()
            res.status_code = 500
            return res

    def post(self):
        # Valida que la petición sea <application/json>
        if request.content_type != "application/json":
            res = make_response()
            res.status_code = 422
            return res
        else:
            # Obtiene la información del request
            json_data = request.get_json(force=True)
            if not json_data:
                res = make_response()
                res.status_code = 422
                return res
            # validamos y deserializamos el request
            data, errors = schema.load(json_data)

            if errors:
                return errors, 422
            try:
                email, password = data['email'], data['password']
                # Consulta si existe algún email igual
                query_set = Users.query.filter_by(email=email).first()
                # Validación con expresión regular
                pw_validate = validate_password(password)
                if not pw_validate:
                    res = jsonify({"mensaje": "La contraseña es incorrecta"})
                    res.status_code = 422
                    return res

                if query_set is None:
                    # Crear el nuevo user
                    password_sha = encrypt_sha512(password, 10000, 10)
                    user = Users(
                        email=email,
                        password=password_sha
                    )
                    user.add(user)
                    query = Users.query.get(user.id)
                    res = schema.dump(query).data
                    return res, 201
                else:
                    res = jsonify({'mensaje': 'El usuario ya existe'})
                    res.status_code = 409
                    return res

            except Exception as e:
                res = make_response()
                res.status_code = 500
                return res


class UserDetail(Resource):
    def get(self, id):
        try:
            # Consulta de User con <id>
            query_set = Users.query.get(id)
            if query_set is None:
                res = make_response()
                res.status_code = 404
                return res
            else:
                # Serialización del query set
                res = schema.dump(query_set).data
                res.status_code = 200
                return res
        except Exception as e:
            # Exception si falla la conexión
            res = make_response()
            res.status_code = 500
            return res

    def put(self, id):
        # Valida que la petición sea <application/json>
        if request.content_type != "application/json":
            res = make_response()
            res.status_code = 422
            return res
        else:
            json_data = request.get_json(force=True)
            # Obtiene la información del request
            if not json_data:
                res = make_response()
                res.status_code = 422
                return res
            # validamos y deserializamos el request
            data, errors = schema.load(json_data)
            if errors:
                return errors, 422
            try:
                user = Users.query.get(id)
                if user is None:
                    res = make_response()
                    res.status_code = 404
                    return res
                email, password = data['email'], data['password']
                pw_validate = validate_password(password)
                if not pw_validate:
                    res = jsonify({"error": "Contraseña no valida"})
                    res.status_code = 422
                    return res
                password_sha = encrypt_sha512(password, 10000, 10)
                setattr(user, 'email', email)
                setattr(user, 'password', password_sha)
                user.update()
                return self.get(id)
            except Exception as e:
                res = make_response()
                res.status_code = 500
                return res

    def delete(self, id):
        try:
            user = Users.query.get(id)
            if user is None:
                res = make_response()
                res.status_code = 404
                return res
            else:
                delete = user.delete(user)
                res = make_response()
                res.status_code = 204
                return res
        except Exception as e:
            # Exception si falla la conexión
            res = make_response()
            res.status_code = 500
            return res


api.add_resource(UsersList, '')
api.add_resource(UserDetail, '/<int:id>')
