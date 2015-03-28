# music_tracker/__init__.py
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
CsrfProtect(app)

mail = Mail(app)

db = SQLAlchemy(app)

from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

from . import views
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()
