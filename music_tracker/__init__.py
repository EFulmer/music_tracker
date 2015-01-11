# music_tracker/__init__.py
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from . import views

db = SQLAlchemy(app)
