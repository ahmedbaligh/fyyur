import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Make sure DATABASE URI is set
if not os.environ.get("DB_CONN_STR"):
    raise RuntimeError("DB_CONN_STR is not set")

# IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_CONN_STR")
SQLALCHEMY_TRACK_MODIFICATIONS = False
