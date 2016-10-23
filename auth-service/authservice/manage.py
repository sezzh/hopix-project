#! /usr/bin/python
""" script de migración de las tablas a la base de datos
"""
from authservice.superusers.models import engine, Base

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
