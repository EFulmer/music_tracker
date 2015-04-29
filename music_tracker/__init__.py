# music_tracker/__init__.py # -*- coding: utf-8 -*-
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

if os.environ.get('HEROKU'):
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
    app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
else:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

CsrfProtect(app)

mail = Mail(app)

db = SQLAlchemy(app)

from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()

from . import views
from .models import User
