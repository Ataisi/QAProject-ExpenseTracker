# importing modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# adding configuration for using a sqlite database
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data.db"))

app.config['SQLALCHEMY_DATABASE_URI'] = database_file #"sqlite:///dat_a.db"
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

from application import routes