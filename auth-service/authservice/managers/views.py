from flask import Blueprint, request, jsonify, make_response
from authservice.managers.models import Managers, ManagersSchema, db
from flask_restful import Api, Resource

from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

managers = Blueprint('managers', __name__)
schema = ManagersSchema()
api = Api(managers)


# http://jsonapi.org/format
# Recurso de los Managers

class ManagersList(Resource):
    def get(self):
        managers_query = Managers.query.all()
        results = schema.dump(managers_query, many=True).data
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                manager_dict = raw_dict['data']['attributes']
                manager = Managers(
                    manager_dict['email'],
                    manager_dict['name'],
                    manager_dict['is_active'],
                    manager_dict['password']
                    )
                # import pdb; pdb.set_trace()
                manager.add(manager)
                query = Managers.query.get(manager.id)
                results = schema.dump(query).data
                return results, 201

        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 403
                return resp

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 403
                return resp


class ManagersUpdate(Resource):
    def get(self, id):
        manager_query = Managers.query.get_or_404(id)
        result = schema.dump(manager_query).data
        return result

    def patch(self, id):
        manager = Managers.query.get_or_404(id)
        raw_dict = request.get_json(force=True)

        try:
            schema.validate(raw_dict)
            manager_dict = raw_dict['data']['attributes']

            for key, value in manager_dict.items():
                setattr(manager, key, value)
            manager.update()
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
        manager = Managers.query.get_or_404(id)
        try:
            delete = manager.delete(manager)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp


api.add_resource(ManagersList, '.json')
api.add_resource(ManagersUpdate, '/<int:id>.json')
