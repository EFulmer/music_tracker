from .music_tracker import app

@app.route('/artist/<string:artist>')
def get_artist_info(artist):
    # replace _ with spaces in case we get kanye_west or something
    # TODO : capitalize properly
    album = lastfm.get_top_album(artist.replace('_', ' '))
    return render_template('artist_info.html', artist=artist, album=album)
