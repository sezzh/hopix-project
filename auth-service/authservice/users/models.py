# -*- encoding: utf-8 -*-
from marshmallow import Schema, fields, ValidationError
from sqlalchemy.exc import SQLAlchemyError
from collections import OrderedDict
from authservice import db


class CRUD():

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Users(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self,  email, password):

        self.email = email
        self.password = password


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Dato no proporcionado.')


# Schema Users

class UsersSchema(Schema):
    # atributo id autoincrementable y de solo lectura dump_only=True
    id = fields.Integer(dump_only=True)
    email = fields.Email(
        required=True,
        validate=must_not_be_blank,
        load_from='sub',
        dump_to='sub'
    )
    password = fields.String(
        required=True,
        load_only=True,
        validate=must_not_be_blank
    )
    is_active = fields.Boolean(dump_only=True)

    class Meta:
        type_ = 'users'
        fields = ("id", "email", "is_active", "password")
        ordered = True
