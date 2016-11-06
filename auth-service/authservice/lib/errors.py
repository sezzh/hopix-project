# -*- encoding: utf-8 -*-
from flask import jsonify


def error_409(msj):
    response = jsonify({"error": msj})
    response.status_code = 409
    return response


def error_410():
    response = jsonify(
        {"error": {"recurso": ["El recurso solicitado no existe."]}}
    )
    response.status_code = 410
    return response


def error_422(error):
    response = jsonify({"error": error})
    response.status_code = 422
    return response


def error_500():
    response = jsonify(
        {"error": {"BD": ["Sin conexión."]}}
    )
    response.status_code = 500
    return response
