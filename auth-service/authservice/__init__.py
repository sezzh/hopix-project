from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response
from authservice.lib import encrypt

db = SQLAlchemy()

encrypt = encrypt

# http://flask.pocoo.org/docs/0.11/patterns/appfactories/


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db.init_app(app)

    # Blueprints
    from authservice.superusers.views import superusers
    # from authservice.managers.views import managers
    from authservice.auth.views import tokens
    app.register_blueprint(superusers, url_prefix='/api/v1/superusers')
    # app.register_blueprint(managers, url_prefix='/api/v1/managers')
    app.register_blueprint(tokens, url_prefix='/auth/tokens')
    return app
