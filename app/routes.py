"""Flask Routes."""
from flask import render_template
from app import app
from app.forms import VisaApplicationForm
from app.users import User

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    visa_form = VisaApplicationForm()
    if visa_form.validate_on_submit():
        user = User(flask_config=app.config, form=visa_form)
        return render_template('success.html', email=user.email)
    return render_template('form.html', form=visa_form)
