from flask import Blueprint, request, jsonify, make_response
from authservice.superusers.models import Superusers, SuperusersSchema, db
from flask_restful import Api, Resource

from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

superusers = Blueprint('superusers', __name__)
schema = SuperusersSchema()
api = Api(superusers)


# http://jsonapi.org/format
# Recurso de los Superusers

class SuperusersList(Resource):
    def get(self):
        superusers_query = Superusers.query.all()
        results = schema.dump(superusers_query, many=True).data
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                superuser_dict = raw_dict['data']['attributes']
                superuser = Superusers(
                    superuser_dict['email'],
                    superuser_dict['name'],
                    superuser_dict['is_active'],
                    superuser_dict['password']
                    )
                # import pdb; pdb.set_trace()
                # superuser.add(superuser)
                # query = Superusers.query.get(superuser.id)
                # results = schema.dump(query).data
                # return results, 201
                resp = (
                    jsonify(
                        {"error": "The method is not allowed"
                            " for the requested URL."}
                    )
                )
                resp.status_code = 403
                return resp

        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 403
                return resp

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 403
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


api.add_resource(SuperusersList, '.json')
api.add_resource(SuperusersUpdate, '/<int:id>.json')
