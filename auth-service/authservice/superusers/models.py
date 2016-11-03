# -*- encoding: utf-8 -*-
from marshmallow import Schema, fields, ValidationError
from collections import OrderedDict
from authservice import db


class CRUD():

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Superusers(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    creation_time = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable='False'
    )
    is_active = db.Column(
        db.Boolean,
        server_default='True',
        nullable=False
    )
    password = db.Column(db.Text(), nullable=False)

    def __init__(self,  username, email, password):

        self.username = username
        self.email = email
        self.password = password


# Custom validador

def must_not_be_blank(data):
    if not data:
        raise ValidationError('Dato no proporcionado.')


# Schema Superusers

class SuperusersSchema(Schema):
    # atributo id autoincrementable y de solo lectura dump_only=True
    id = fields.Integer(dump_only=True)
    username = fields.String(
        validate=must_not_be_blank,
        load_from='sub', dump_to='sub'
    )
    email = fields.Email(validate=must_not_be_blank)
    is_active = fields.Boolean(dump_only=True)

    class Meta:
        type_ = 'superusers'
        fields = ("id", "username", "email", "is_active")
        ordered = True
