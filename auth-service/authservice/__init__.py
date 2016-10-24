from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authservice.superusers import superusers
from authservice.managers import managers
from authservice.authorizations import authorizations


app = Flask(__name__)
app.register_blueprint(superusers)
app.register_blueprint(managers)
app.register_blueprint(authorizations)
