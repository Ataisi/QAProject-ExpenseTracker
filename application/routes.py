from application import app
from flask import render_template, request, url_for, redirect

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/addexpense')
def add_expense():
    return render_template('addexpense.html')

@app.route('/viewexpense')
def view_expense():
    return render_template('viewexpense.html')

