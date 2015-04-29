# config.py
# -*- coding: utf-8 -*-
import os

DEBUG = True
SQLALCHEMY_ECHO = False
BCRYPT_LOG_ROUNDS = 12

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
