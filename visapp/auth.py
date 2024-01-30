from flask import Blueprint
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
# from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, current_app
# from visapp.auth import bp
import os
# from flask import current_app as app
# print("TESTINGFG")
# print(current_app.config["AUTH0_CLIENT_ID"])

bp = Blueprint('auth', __name__)
def init_app(oauth):
    oauth.register(
        "auth0",
        client_id=os.environ.get("AUTH0_CLIENT_ID"),
        client_secret=os.environ.get("AUTH0_CLIENT_SECRET"),
        client_kwargs={
            "scope": "openid profile email",
        },
        server_metadata_url=f'https://{os.environ.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
    )

# oauth = current_app.extensions["oauth"]

@bp.route("/")
def home():
    return render_template("index.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

@bp.route("/login")
def login():
    print(current_app.config["AUTH0_CLIENT_ID"] + "hello from login route")
    for key in current_app.extensions: print("extensions:" + key)
    oauth = current_app.extensions["authlib.integrations.flask_client"]
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("auth.callback", _external=True)
    )

@bp.route("/callback", methods=["GET", "POST"])
def callback():
    with current_app.app_context():
        oauth = current_app.extensions["authlib.integrations.flask_client"]
        token = oauth.auth0.authorize_access_token()
        session["user"] = token
        return redirect("/form")

# @bp.route("/logout")
# def logout():
#     session.clear()
#     return redirect(
#         "https://" + os.environ.get("AUTH0_DOMAIN")
#         + "/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": url_for("home", _external=True),
#                 "client_id": os.environ.get("AUTH0_CLIENT_ID"),
#             },
#             quote_via=quote_plus,
#         )
#     )

