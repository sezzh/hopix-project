#! /usr/bin/env python
""" script de migración de las tablas a la base de datos
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from runserver import app
from authservice.superusers.models import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
