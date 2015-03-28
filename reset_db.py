import os

from music_tracker import db

os.remove('instance/app.db')
db.create_all()
