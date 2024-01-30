"""To start the application."""
from flask import Flask
from visapp.config import Config
from visapp import auth
import os
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config.from_object(Config)

oauth = OAuth(app)
auth.init_app(oauth)

app.register_blueprint(auth.bp)
