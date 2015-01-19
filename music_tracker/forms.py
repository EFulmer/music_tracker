# music_tracker/forms.py
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class EnterArtistForm(Form):
    artist = StringField('artist', validators=[DataRequired()])
    # submit = SubmitField('Get Artist Info')


# lifted from Explore Flask: https://exploreflask.com/forms.html
class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ArtistInfoForm(Form):
    submit = SubmitField('Track Artist')


class ArtistEntryField(Form):
    deactivate = BooleanField('Archive')
    delete = BooleanField('Delete')

