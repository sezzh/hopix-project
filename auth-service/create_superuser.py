#! /usr/bin/env python
from authservice.superusers.models import Superusers
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

""" Función para la creación de los superuser.
"""


def manager():
    print("New superuser")
    email = input("email: ")
    name = input("Name: ")
    password = input("Password: ")
    superuser = Superusers(
        email, name=name, is_active='True', password=password
    )
    session.add(superuser)
    session.commit()

if __name__ == '__main__':
    manager()
