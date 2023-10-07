"""Flask configuration variables."""
from os import environ, path

"""Set Flask configuration from .env file."""

# General Config
FLASK_APP = "app"
FLASK_DEBUG = True

# Database
SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"
