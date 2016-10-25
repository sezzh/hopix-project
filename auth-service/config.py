# Configuración de la base de datos
# Variables de conexión
pg_db_username = 'test'
pg_db_password = 'test'
pg_db_name = 'test'
pg_db_hostname = 'authservice_db'

# Variables Flask
DEBUG = True
PORT = 5000
HOST = "0.0.0.0"

# Variables SQLALCHEMY
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "My Secret key"

# Variable de conexión de SQLALCHEMY para PostgreSQL
SQLALCHEMY_DATABASE_URI = (
    "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=pg_db_username,
        DB_PASS=pg_db_password,
        DB_ADDR=pg_db_hostname,
        DB_NAME=pg_db_name
    )
)
