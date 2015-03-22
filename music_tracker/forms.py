# music_tracker/forms.py
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import BooleanField, DateTimeField, FieldList, \
        FormField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class EnterArtistForm(Form):
    artist = StringField('artist', validators=[DataRequired()])
    submit = SubmitField('Get Artist Info')


class AddArtistForm(Form):
    submit = SubmitField('Add {} To Your List')


# lifted from Explore Flask: https://exploreflask.com/forms.html
class EmailPasswordForm(Form):
    email    = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ArtistInfoForm(Form):
    submit = SubmitField('Track Artist')


class ArtistField(Form):
    # artist_name = StringField('Artist Name')
    # album       = StringField('Top Album')
    # song        = StringField('Top Song')
    # added       = DateTimeField('Date Added')
    artist_name = ''
    album       = ''
    song        = ''
    added       = ''
    deactivate  = BooleanField('Archive', default=False)
    delete      = BooleanField('Delete', default=False)


class ManageArtistsForm(Form):
    artists = FieldList(FormField(ArtistField))
    submit = SubmitField('Update')

