"""To start the application."""
from flask import Flask
from visapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from visapp import routes
