import os, shortuuid
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename

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
def upload_file():
    if request.method == 'POST':
        unique_id = str(shortuuid.uuid())
        user_folder = os.path.join(app.config['USERS_FOLDER'], unique_id)

        os.mkdir(user_folder)

        face_image_filepath = os.path.join(user_folder, unique_id + '_face_image.jpg')
        passport_image_filepath = os.path.join(user_folder, unique_id + '_passport_image.jpg')
        face_image_filename = unique_id + '_face_image.jpg'
        request.files['face_image'].save(os.path.join(user_folder, face_image_filename))
        passport_image_filename = unique_id + '_passport_image.jpg'
        request.files['passport_image'].save(os.path.join(user_folder, passport_image_filename))

        user_data = {
            'full_name': request.form['full_name'],
            'email': request.form['email'],
            'passport_number': request.form['passport_number'],
            'dob': request.form['dob'],
            'nationality': request.form['nationality'],
            'visa_type': request.form['visa_type'],
            'processing_time': request.form['processing_time'],
            'port_of_arrival': request.form['port_of_arrival'],
            'face_image_filepath': face_image_filepath,
            'passport_image_filepath': passport_image_filepath,
        }
        
        return render_template('success.html', unique_id=unique_id)
    
    return render_template('form.html')
