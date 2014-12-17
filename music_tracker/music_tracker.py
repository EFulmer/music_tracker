# -*- coding: utf-8 -*-

from contextlib import closing
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

import config
import lastfm


app = Flask(__name__)
app.config.from_object(config)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/artist/<string:artist>')
def get_artist_info(artist):
    # replace _ with spaces in case we get kanye_west or something
    # TODO : capitalize properly
    album = lastfm.get_top_album(artist.replace('_', ' '))
    return render_template('artist_info.html', artist=artist, album=album)


if __name__ == '__main__':
    init_db()
    app.run()
