<<<<<<< HEAD
from unicodedata import category
from application import app
from flask import render_template, request, url_for, redirect
from datetime import date
from application import db

from application.models import Expenses, Category
=======
from application import app
from flask import render_template, request, url_for, redirect
>>>>>>> db7ca7862b2bf56a054f0454c7c146510f4a22ad

@app.route('/')
def home_page():
    return render_template('home.html')

<<<<<<< HEAD




#  routes to the addexpense page
@app.route('/addexpense' , methods = ['GET','POST'])
def add_expense():
    if request.method == 'GET':
        return render_template('addexpense.html')
    print(request.form['purchased_date'])
 # method to add a new expense entry
    if request.method == 'POST':
        purchase_date = request.form['purchased_date']
        item = request.form['item']
        description = request.form['description']
        category_name = request.form['category']
        quantity = request.form['quantity']
        unit_price = request.form['unit_price']
        amount = request.form['amount']

        new_expense = Expenses(purchase_date=purchase_date, item=item, description=description, category_id = category_name, quantity=quantity, unit_price=unit_price, amount=amount)
        db.session.add(new_expense)
        db.session.commit()
        return redirect('/')   #clear page for new entry

# view expenses
@app.route('/viewexpense')
def view_expense():
    display_expenses = Expenses.query.all()
    return render_template('viewexpense.html', data=enumerate(display_expenses,1))

# add expenses test
@app.route('/test')
def test():
    purchase_date = '2020-10-20'
    item = 'rice'
    description = '20kg from Tesco'
    category_name = 1
    quantity = 1
    unit_price = 5
    amount = 5

    new_expense = Expenses(purchase_date=purchase_date, item=item, description=description, category_id = category_name, quantity=quantity, unit_price=unit_price, amount=amount)
    db.session.add(new_expense)
    db.session.commit()
    # cc = Category(category_name='test')
    # Category.query.all()
    return "<h1>done!<h1>"

=======
@app.route('/addexpense')
def add_expense():
    return render_template('addexpense.html')

@app.route('/viewexpense')
def view_expense():
    return render_template('viewexpense.html')
>>>>>>> db7ca7862b2bf56a054f0454c7c146510f4a22ad

