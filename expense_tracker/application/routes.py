from application import app, db
from flask import render_template, request, url_for, redirect
# from application.models import Category, Expenses
from sqlalchemy.sql import text

@app.route('/addexpense')
def addexpense():

@app.route('/home')
def home():
    return render_template('home.html')


    l