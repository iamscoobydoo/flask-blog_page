from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from wtforms.widgets.core import SubmitInput

class BlogPostForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    text = TextAreaField('Text: ', validators=[DataRequired()])
    submit = SubmitField('Post')