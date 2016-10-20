from flask import Flask
from authservice.api_test import api_test


app = Flask(__name__)
app.register_blueprint(api_test, url_prefix='/test')
