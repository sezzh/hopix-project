from flask import Flask
from authservice.superusers import superusers
from authservice.managers import managers


app = Flask(__name__)
app.register_blueprint(superusers)
app.register_blueprint(managers)
