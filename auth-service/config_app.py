# -*- encoding: utf-8 -*-
from config_env_app import (
    pg_db_username, pg_db_password, pg_db_name,
    pg_db_hostname, authservice_flask_secret
)


# Variables Flask
PORT = 5000
HOST = "0.0.0.0"
SECRET_KEY = authservice_flask_secret

# Variables SQLALCHEMY
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Variable de conexión de SQLALCHEMY para PostgreSQL
SQLALCHEMY_DATABASE_URI = (
    # Configuración de la base de datos
    "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=pg_db_username,
        DB_PASS=pg_db_password,
        DB_ADDR=pg_db_hostname,
        DB_NAME=pg_db_name
    )
)
