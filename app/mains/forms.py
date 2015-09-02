from flask_wtf import Form
from wtforms import StringField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Optional, Length, Email, Regexp
from wtforms import ValidationError

class SearchForm(Form):
    search = StringField('Search', validators=[
        InputRequired('Your input is required')
    ])
    submit = SubmitField('Search')

