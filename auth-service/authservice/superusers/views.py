# -*- encoding: utf-8 -*-
from flask import Blueprint, request, jsonify
from authservice.superusers.models import Superusers, SuperusersSchema, db
from flask_restful import Api, Resource

superusers = Blueprint('superusers', __name__)
schema = SuperusersSchema()
api = Api(superusers)


# Recurso de los Superusers

class SuperusersList(Resource):
    def get(self):
        try:
            superusers_query = Superusers.query.all()
            # Serialize the queryset
            resp = schema.dump(superusers_query, many=True).data
            return resp
        except Exception as e:
            resp = jsonify({"mensaje": " ¡ No tenemos conexión a la BD :( !"})
            resp.status_code = 500
            return resp

api.add_resource(SuperusersList, '')
