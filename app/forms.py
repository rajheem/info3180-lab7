from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired,Email,DataRequired


class UploadForm(FlaskForm):
    description=TextAreaField('description',validators=[DataRequired()])
    photo=FileField('photo',
    validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
