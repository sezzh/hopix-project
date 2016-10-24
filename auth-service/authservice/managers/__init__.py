from flask import (
    request, g, Blueprint, jsonify
)

managers = Blueprint('managers', __name__)


@managers.route('/managers')
def manager():
    return jsonify(message='managers')
