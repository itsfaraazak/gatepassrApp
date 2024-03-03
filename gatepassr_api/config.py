"""Flask App configuration."""
from os import environ, path
from dotenv import load_dotenv

# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
print(basedir)
print(load_dotenv)

"""Set Flask config variables."""

# General Config
ENVIRONMENT = environ.get("ENVIRONMENT")
FLASK_APP = environ.get("FLASK_APP")
FLASK_DEBUG = environ.get("FLASK_DEBUG")
JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")

# Database
POSTGRES_HOST_URI = environ.get('POSTGRES_HOST_URI')
POSTGRES_DATABASE_NAME = environ.get('POSTGRES_DATABASE_NAME')
POSTGRES_USERNAME = environ.get('POSTGRES_USERNAME')
POSTGRES_PASSWD = environ.get('POSTGRES_PASSWD')

# Frontend
FRONTEND_URL = environ.get('FRONTEND_URL')
