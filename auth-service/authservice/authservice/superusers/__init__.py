from flask import (
    request, g, Blueprint, jsonify
)

superusers = Blueprint('superusers', __name__)


@superusers.route('/superusers')
def superuser():
    return jsonify(message='superusers')
