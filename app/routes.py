from app import app
from flask import render_template
from app.forms import VisaApplicationForm
from app.users import User

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = VisaApplicationForm()
    if form.validate_on_submit():
        user = User(flask_config=app.config, form=form)
        return render_template('success.html', email=user.email)
    return render_template('form.html', form=form)
