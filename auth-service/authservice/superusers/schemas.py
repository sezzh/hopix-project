from marshmallow import Schema, fields

""" Archivo serializador para el modelo de Superuser
"""


class SuperuserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)


superusers_schema = SuperuserSchema(many=True, only=('id', 'name'))
superuser_schema = SuperuserSchema()
