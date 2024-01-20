import os, shortuuid, json
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, DateField, SubmitField, EmailField
from wtforms.validators import DataRequired, InputRequired, Length
from werkzeug.utils import secure_filename

def return_user_folder(user_id):
    user_folder_filepath = os.path.join(app.config['USERS_FOLDER'], user_id)
    return user_folder_filepath

def make_user_folder(user_id):
    user_folder_filepath = return_user_folder(user_id=user_id)
    try:
        os.mkdir(user_folder_filepath)
    except Exception as e:
        print(e)
    return user_folder_filepath

def save_json_user_data(user_id, json_user_data, filename_ending='_user_data.json'):
    json_user_data_filepath = os.path.join(return_user_folder(user_id=user_id), user_id + filename_ending)
    with open(json_user_data_filepath, 'w', encoding='utf-8') as file:
        json.dump(json_user_data, file, indent=4, sort_keys=True, default=str)
    return json_user_data_filepath

def secure_user_email(email):
    email = email.replace('@', '_')
    email = email.replace('.', '_')
    return secure_filename(email)

def make_json_data(form):
    json_data = {}
    for field in form:
        json_data[field.name] = field.data
    return json_data

class application_form(FlaskForm):
    full_name = StringField('Full Name:', validators=[DataRequired(), Length(min=3, max=100)])
    email = EmailField('Email:', validators=[DataRequired()])
    passport_number = StringField('Passport Number:', validators=[DataRequired(), Length(min=3, max=9)])
    dob = DateField('Date of Birth:', validators=[DataRequired()])
    face_image = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit')

USERS_FOLDER = './users'
ALLOWED_EXTENSIONS = {'heic', 'HEIC', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.config['USERS_FOLDER'] = USERS_FOLDER

# The code below will limit the maximum allowed payload to 16 megabytes.
# If a larger file is transmitted, Flask will raise a RequestEntityTooLarge exception.
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = application_form()
    if form.validate_on_submit():
        user_id = secure_user_email(email=form.email.data)
        make_user_folder(user_id=user_id)
        save_json_user_data(user_id=user_id, json_user_data=make_json_data(form=form))
        
        # user_folder = os.path.join(app.config['USERS_FOLDER'], unique_id)


        # face_image_filepath = os.path.join(user_folder, unique_id + '_face_image.jpg')
        # passport_image_filepath = os.path.join(user_folder, unique_id + '_passport_image.jpg')
        
        # face_image_filename = unique_id + '_face_image.jpg'
        # request.files['face_image'].save(os.path.join(user_folder, face_image_filename))
        # passport_image_filename = unique_id + '_passport_image.jpg'
        # request.files['passport_image'].save(os.path.join(user_folder, passport_image_filename))



        return render_template('success.html', email=form.email.data, passport_number=form.passport_number.data)
    return render_template('form.html', form=form)
