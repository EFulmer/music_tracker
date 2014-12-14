# -*- coding: utf-8 -*-

from contextlib import closing
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

import config
import lastfm


app = Flask(__name__)
app.config.from_object(config)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/artist_info')
def get_artist_info():
    artistname = request.args.get('name')
    if artistname:
        return lastfm.get_top_album(artistname)
    return 'TODO'


if __name__ == '__main__':
    app.run()
