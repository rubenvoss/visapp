from flask import Blueprint

bp = Blueprint('forms', __name__, template_folder='templates')

from app.forms import email