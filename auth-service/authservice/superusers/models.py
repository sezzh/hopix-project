#! /usr/bin/python3.5
from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.types import password
from passlib.hash import pbkdf2_sha512, md5_crypt
from sqlalchemy_utils import Password, PasswordType

Base = declarative_base()
Column(Integer, Sequence('superuser_id_seq'), primary_key=True)
engine = create_engine(
    "postgresql://test:test@authservice_db/test?client_encoding=utf8"
    )


class Superuser(Base):
    __tablename__ = 'superuser'
    id = Column(Integer, Sequence('superuser_id_seq'), primary_key=True)
    name = Column(String)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
            ],
        deprecated=['md5_crypt']
    ))
