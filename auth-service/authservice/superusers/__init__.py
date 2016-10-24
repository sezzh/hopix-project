from flask import (
    request, g, Blueprint, jsonify, flash
)
# from authservice.superusers import models
from authservice.superusers.models import Superuser, engine
from authservice.superusers import schemas

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


superusers = Blueprint('superusers', __name__)


@superusers.route('/superusers')
def get_superuser():
    records = session.query(Superuser).order_by(Superuser.id)
    result = schemas.superusers_schema.dump(records)
    return jsonify({'superusers': result.data})
