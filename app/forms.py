from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, DateField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length

class ApplicationForm(FlaskForm):
    full_name = StringField('Full Name:', validators=[DataRequired(), Length(min=3, max=100)])
    email = EmailField('Email:', validators=[DataRequired()])
    passport_number = StringField('Passport Number:', validators=[DataRequired(), Length(min=3, max=9)])
    dob = DateField('Date of Birth:', validators=[DataRequired()])
    face_image = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit')
