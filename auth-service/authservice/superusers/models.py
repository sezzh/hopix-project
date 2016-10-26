from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy_utils.types import password
# from passlib.hash import pbkdf2_sha512, md5_crypt
# from sqlalchemy_utils import Password, PasswordType
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


class Superusers(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    creation_time = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable=False
    )
    is_active = db.Column(
        db.Boolean,
        server_default="false",
        nullable=False
    )
    password = db.Column(db.Text(), nullable=False)

    def __init__(self,  email,  name, is_active, password):

        self.email = email
        self.name = name
        self.is_active = is_active
        self.password = password


class SuperusersSchema(Schema):
    not_blank = validate.Length(min=1, error='Este campo no debe estar vacío')
    id = fields.Integer(dump_only=True)
    email = fields.Email(validate=not_blank)
    name = fields.String(validate=not_blank)
    is_active = fields.Boolean()
    password = fields.String(validate=not_blank)

    # self links

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/superusers/"
        else:
            self_link = "/superusers/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'superusers'
