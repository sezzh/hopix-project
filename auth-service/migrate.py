#!/usr/bin/env python
# -*- encoding: utf-8 -*-
""" script de migración de las tablas a la base de datos
"""
from authservice.superusers.models import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from runserver import app

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
