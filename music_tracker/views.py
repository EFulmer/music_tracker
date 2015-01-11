from flask import render_template

import lastfm
from . import app


@app.route('/')
def index():
    return 'hello'


@app.route('/artist/<string:artist>')
def artist_info(artist):
    info = lastfm.get_artist_info(artist.replace('_', ' '))
    return render_template('artist_info.html', 
                           artist=info.artist, 
                           album=info.title)


@app.route('/add_artist')
def add_artist():
    pass
