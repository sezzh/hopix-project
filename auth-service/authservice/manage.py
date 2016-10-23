#! /usr/bin/python3.5
from authservice.superuser.models import engine, Base

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
