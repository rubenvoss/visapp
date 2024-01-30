"""Forms with WTForms for the Flask App"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, DateField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length
from flask import render_template, Blueprint

class VisaApplicationForm(FlaskForm):
    full_name = StringField('Full Name:', validators=[DataRequired(), Length(min=3, max=100)])
    email = EmailField('Email:', validators=[DataRequired()])
    passport_number = StringField('Passport Number:', validators=[DataRequired(), Length(max=9)])
    dob = DateField('Date of Birth:', validators=[DataRequired()])
    face_image = FileField('''Clear Image of your face, no Glasses, look straight
                           into Camera''', validators=[FileRequired(['jpg','jpeg','png'])])
    submit = SubmitField('Submit')

bp = Blueprint('forms', __name__)

@bp.route("/form", methods=["GET", "POST"])
def form():
    visa_form = VisaApplicationForm()
    if visa_form.validate_on_submit():
        return render_template('success.html', indent=4)
    return render_template('form.html', form=visa_form)