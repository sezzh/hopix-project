import os

# Configuración de la base de datos
# Variables de conexión Postgres
pg_db_username = os.environ['AUTHSERVICE_PG_USERNAME_SECRET']
pg_db_password = os.environ['AUTHSERVICE_PG_PASSWORD_SECRET']
pg_db_name = os.environ['AUTHSERVICE_PG_NAME_SECRET']
pg_db_hostname = os.environ['AUTHSERVICE_PG_HOST_SECRET']


# Variables Flask
DEBUG = True
PORT = 5000
HOST = "0.0.0.0"
SECRET_KEY = os.environ['AUTHSERVICE_FLASK_SECRET']

# Variables SQLALCHEMY
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Variable de conexión de SQLALCHEMY para PostgreSQL
SQLALCHEMY_DATABASE_URI = (
    "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=pg_db_username,
        DB_PASS=pg_db_password,
        DB_ADDR=pg_db_hostname,
        DB_NAME=pg_db_name
    )
)
