from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
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
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    creation_time = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        nullable='False'
    )
    is_active = db.Column(
        db.Boolean,
        server_default='False',
        nullable=False
    )
    password = db.Column(db.Text(), nullable=False)

    def __init__(self,  username, email, is_active, password):

        self.username = username
        self.email = email
        self.is_active = is_active
        self.password = password


class SuperusersSchema(Schema):
    not_blank = validate.Length(min=1, error='Este campo no debe estar vacío')
    id = fields.Integer(dump_only=True)
    username = fields.String(validate=not_blank)
    email = fields.String(validate=not_blank)
    is_active = fields.Boolean()
    # password = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_url = 'http://localhost:5000/api/v1/superusers'
        else:
            self_url = (
                "http://localhost:5000/api/v1/superusers/{}".format(data['id'])
                )
        return {'self': self_url}

    class Meta:
        type_ = 'superusers'
        # strict = True
