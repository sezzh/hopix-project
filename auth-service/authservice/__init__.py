from flask import Flask, Response
# http://flask.pocoo.org/docs/0.11/patterns/appfactories/


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from authservice.superusers.models import db
    db.init_app(app)

    # Blueprints
    from authservice.superusers.views import superusers
    app.register_blueprint(superusers, url_prefix='/api/v1/superusers')

    return app
