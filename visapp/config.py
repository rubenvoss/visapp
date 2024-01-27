"""Flask configuration variables."""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SESSION_TYPE = os.environ.get('SESSION_TYPE') or 'filesystem'
    USERS_FOLDER = os.environ.get('USERS_FOLDER') or './users'
    MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH') or 16 * 1000 * 1000
    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID') or 'client-id'
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET') or 'secret'
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN') or 'my-domain'
