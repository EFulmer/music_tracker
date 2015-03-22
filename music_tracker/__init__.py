# music_tracker/__init__.py
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
CsrfProtect(app)

db = SQLAlchemy(app)

from . import views
