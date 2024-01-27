"""To start the application."""
from flask import Flask
from visapp.config import Config
from visapp import auth
import os
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
oauth = OAuth(app)

app.config.from_object(Config)
app.register_blueprint(auth.bp)


import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
# from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
oauth.register(
    "auth0",
    client_id=app.config["AUTH0_CLIENT_ID"],
    client_secret=app.config["AUTH0_CLIENT_SECRET"],
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{app.config["AUTH0_DOMAIN"]}/.well-known/openid-configuration'
)

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/form")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + app.config["AUTH0_DOMAIN"]
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": app.config["AUTH0_CLIENT_ID"],
            },
            quote_via=quote_plus,
        )
    )

@app.route("/")
def home():
    return render_template("index.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

from flask import render_template
from visapp import app
from visapp.forms import VisaApplicationForm
from visapp.users import User
@app.route("/form", methods=["GET", "POST"])
# def form():
#     return render_template("form.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))
def form():
    visa_form = VisaApplicationForm()
    if visa_form.validate_on_submit():
        user = User(flask_config=app.config, form=visa_form)
        return render_template('success.html', email=user.email, session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))
    return render_template('form.html', form=visa_form)