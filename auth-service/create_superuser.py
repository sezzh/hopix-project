#! /usr/bin/python
from authservice.superusers.models import Superuser, engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

""" Función para la creación de los superuser.
"""


def manager():
    print("New superuser")
    name = input("Name: ")
    password = input("Password: ")
    superuser = Superuser(name=name, password=password)
    session.add(superuser)
    session.commit()

if __name__ == '__main__':
    manager()
