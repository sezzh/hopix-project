#! /usr/bin/python3.5
from authservice.superuser.models import Superuser, engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


def manager():
    print("New superuser")
    name = input("Name: ")
    password = input("Password: ")
    superuser = Superuser(name=name, password=password)
    session.add(superuser)
    session.commit()

if __name__ == '__main__':
    manager()
