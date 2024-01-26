from flask import Blueprint

bp = Blueprint('auth', __name__)

from visapp.auth import routes
