# create_db.py
# -*- coding: utf-8 -*-
import os.path
from config import SQLALCHEMY_DATABASE_URI
from music_tracker import db


db.drop_all()
db.create_all()
