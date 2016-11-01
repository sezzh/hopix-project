from flask import Blueprint, request, jsonify, make_response
from authservice.superusers.models import Superusers, SuperusersSchema, db
from flask_restful import Api, Resource

from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

from authservice import encrypt

superusers = Blueprint('superusers', __name__)
schema = SuperusersSchema()
api = Api(superusers)


# Recurso de los Superusers


class SuperusersList(Resource):
    def get(self):
        try:
            superusers_query = Superusers.query.all()
            results = schema.dump(superusers_query, many=True).data
            return results
        except Exception as e:
            resp = jsonify({"mensaje": " ¡ No tenemos conexión a la BD :( !"})
            resp.status_code = 500
            return resp


class SuperusersUpdate(Resource):
    def get(self, id):
        superuser_query = Superusers.query.get_or_404(id)
        result = schema.dump(superuser_query).data
        return result

    def patch(self, id):
        superuser = Superusers.query.get_or_404(id)
        raw_dict = request.get_json(force=True)

        try:
            schema.validate(raw_dict)
            superuser_dict = raw_dict['data']['attributes']

            for key, value in superuser_dict.items():
                if key == "password":
                    password = (
                        encrypt.encrypt_sha512(value, 10000, 10)
                    )
                    setattr(superuser, key, password)
                else:
                    setattr(superuser, key, value)
            superuser.update()
            return self.get(id)

        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 401
                return resp

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp

    def delete(self, id):
        superuser = Superusers.query.get_or_404(id)
        try:
            delete = superuser.delete(superuser)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp


api.add_resource(SuperusersList, '')
api.add_resource(SuperusersUpdate, '/<int:id>')
