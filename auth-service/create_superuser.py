#! /usr/bin/env python
from authservice.superusers.models import Superusers
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, or_
from config import SQLALCHEMY_DATABASE_URI
from authservice.lib.encrypt import encrypt_sha512
from authservice.lib.regex_validators import validate_email, validate_password
import getpass

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

""" Función para la creación de los superuser.
"""


def create_superuser():
    print("Nuevo administrador")
    username = input("Ingrese su Username: ")
    email = input("Ingrese su email: ")
    while not validate_email(email):
        print("¡ email incorrecto, veriquelo por favor !")
        email = input("email: ")

    password = getpass.getpass("Ingrese su password: ")
    while not validate_password(password):
        print("¡ Password incorrecto, veriquelo por favor !")
        print("Debe tener 1 letra minuscula y 1 mayuscula")
        print("1 numero y 1 caracter especial !@#$&* ")
        print("Debe ser contener de 8 a 15 caracteres")
        password = getpass.getpass("Ingrese su password: ")

    password = encrypt_sha512(password, 10000, 10)
    try:
        q_username = (
            session.query(Superusers).filter_by(username=username).count()
            )
        q_email = session.query(Superusers).filter_by(email=email).count()
        if q_username > 0 or q_email > 0:
            print("¡ Username o Email, ya existen :( ! Intentelo nuevamente")
        else:
            superuser = Superusers(
                                    username=username,
                                    email=email,
                                    is_active='True',
                                    password=password
                                    )
            try:
                session.add(superuser)
                session.commit()
                print("¡ Administrador creado Correctamente :) ")
                print('Username: {}'.format(username))
                print('Email: {}'.format(email))
            except Exception as e:
                print('¡ Error interno de validación :) ! ')
    except Exception as e:
        print('¡ No tenemos conexión a la BD :( !')


if __name__ == '__main__':
    create_superuser()
