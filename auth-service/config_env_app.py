# -*- encoding: utf-8 -*-
import os

# Clave secreta de la app de Flask
authservice_flask_secret = os.environ['AUTHSERVICE_FLASK_SECRET']

# Variables de conexión Postgres
pg_db_username = os.environ['AUTHSERVICE_DB_USERNAME_SECRET']
pg_db_password = os.environ['AUTHSERVICE_DB_PASSWORD_SECRET']
pg_db_name = os.environ['AUTHSERVICE_DB_NAME_SECRET']
pg_db_hostname = os.environ['AUTHSERVICE_DB_HOST_SECRET']


# Permisos por default de los al crear un superuser
super_permissions = os.environ['AUTHSERVICE_SUPER_PERMISSIONS_SECRET']
