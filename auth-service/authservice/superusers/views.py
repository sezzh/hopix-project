# -*- encoding: utf-8 -*-
from flask import Blueprint, request, make_response, jsonify
from authservice.superusers.models import Superusers, SuperusersSchema, db
from flask_restful import Api, Resource
from authservice.lib.encrypt import encrypt_sha512
from authservice.lib.regex_validators import validate_password


superusers = Blueprint('superusers', __name__)
schema = SuperusersSchema()
api = Api(superusers)


# Recurso de los Superusers

class SuperusersList(Resource):
    def get(self):
        try:
            # Consulta de todos los Superusers
            query_set = Superusers.query.all()
            # Serializamos el query set indicando con many que es un array
            res = schema.dump(query_set, many=True).data
            return res, 200
        except Exception as e:
            # Excepción si falla la conexión
            res = make_response()
            res.status_code = 500
            return res


class SuperuserDetail(Resource):
    def get(self, id):
        try:
            # Consulta del Superuser con <id>
            query_set = Superusers.query.get(id)
            if query_set is None:
                res = make_response()
                res.status_code = 404
                return res
            else:
                # Selización del query set
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
                superuser = Superusers.query.get(id)
                if superuser is None:
                    res = make_response()
                    res.status_code = 404
                    return res
                username, email, password = (
                    data['username'], data['email'], data['password']
                )
                pw_validate = validate_password(password)
                if not pw_validate:
                    res = jsonify({"Contraseña no valida"})
                    res.status_code = 422
                    return res
                password_sha = encrypt_sha512(password, 10000, 10)
                setattr(superuser, 'username', username)
                setattr(superuser, 'email', email)
                setattr(superuser, 'password', password_sha)
                superuser.update()
                return self.get(id)
            except Exception as e:
                res = make_response()
                res.status_code = 500
                return res

    def delete(self, id):
        try:
            superuser = Superusers.query.get(id)
            if superuser is None:
                res = make_response()
                res.status_code = 404
                return res
            else:
                delete = superuser.delete(superuser)
                res = make_response()
                res.status_code = 204
                return res
        except Exception as e:
            # Exception si falla la conexión
            res = make_response()
            res.status_code = 500
            return res


api.add_resource(SuperusersList, '')
api.add_resource(SuperuserDetail, '/<int:id>')
