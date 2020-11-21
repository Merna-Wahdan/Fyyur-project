import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'postgres://ahmad@localhost:5432/todoapp'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
