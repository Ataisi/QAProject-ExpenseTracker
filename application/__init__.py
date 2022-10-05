# importing modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

from application import routes