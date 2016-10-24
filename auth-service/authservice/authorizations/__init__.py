from flask import (
    request, g, Blueprint, jsonify
)

authorizations = Blueprint('authorizations', __name__)


@authorizations.route('/authorizations')
def authenticate():
    return jsonify(message='Authenticate')
