from sqlalchemy import null
from application import app, db
from flask import render_template, request, url_for, redirect
#from application.forms import AddExpenseForm
#from application.models import Category, Expenses
from datetime import date

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# routing to the add expense page
@app.route('/addexpense')
def addexpense():
    return render_template('addexpense.html')

# @app.route('/addentry', methods = ['POST', 'GET'])
# def add_entry():
#     message = ""
#     form = AddExpenseForm(request.form)

#     if request.method == "POST":
#         purchase_date = request.form['purchase_date']
#         item = request.form['item']
#         description = request.form['description']
#         category = request.form['category']
#         quantity = request.form['quantity']
#         unit_price = request.form['unit_price']
#         amount = request.form['amount']

#         if amount == null and unit_price != null:
#             return amount == unit_price * quantity
#         elif amount != null and unit_price != null:
#             return amount == unit_price * quantity
#         else:
#             amount < 0 and unit_price < 0
#             amount == unit_price * quantity





@app.route('/viewexpense')
def viewexpense():
    return render_template('viewexpense.html')

