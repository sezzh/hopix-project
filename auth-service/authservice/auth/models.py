from marshmallow_jsonapi import Schema, fields
from marshmallow import validate


class TokenSchema(Schema):
    not_blank = validate.Length(min=1, error='Este campo no debe estar vacío')
    id = fields.Integer(dump_only=True)
    email = fields.Email(validate=not_blank)
    name = fields.String(validate=not_blank)
    password = fields.String()

    class Meta:
        type_ = 'superusers'
