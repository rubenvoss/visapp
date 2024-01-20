from app import app
from flask import render_template
from app.forms import ApplicationForm
from app.users import User

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = ApplicationForm()
    if form.validate_on_submit():
        user_id = secure_user_email(email=form.email.data)
        make_user_folder(user_id=user_id)
        save_json_user_data(user_id=user_id, json_user_data=make_json_data(form=form))
        save_image()
        return render_template('success.html', email=form.email.data, passport_number=form.passport_number.data)
    return render_template('form.html', form=form)
