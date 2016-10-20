from flask import (
    request, g, Blueprint, jsonify
)

api_test = Blueprint('api_test', __name__)


@api_test.route('/')
def hello():
    return jsonify(message='holi')
