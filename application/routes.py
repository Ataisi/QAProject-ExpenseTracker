
from application import app
from flask import render_template, request, url_for, redirect
from datetime import date
from application import db

from application.models import Expenses, Category

@app.route('/')
def home_page():
     return render_template('home.html')





#  routes to the addexpense page
@app.route('/addexpense' , methods = ['GET','POST'])
def add_expense():
    if request.method == 'GET':
        return render_template('addexpense.html')
   
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
        return render_template('/addexpense.html')   

# view expenses
@app.route('/viewexpense')
def view_expense():
    display_expenses = Expenses.query.all()
    return render_template('viewexpense.html', data=enumerate(display_expenses,1))

# 
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update():
#     if request.method == 'GET':
#         exp = Expenses.query.filter_by(id=id).first()
#         #if request.method=='POST':
#         if exp:
#             return render_template('update.html', expense=exp)
#         else:
#             return abort(404)
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
     expense = Expenses.query.filter_by(id=id).first()
     if request.method == 'POST':
        if expense:
            db.session.delete(expense)
            db.session.commit()

            purchase_date = request.form['purchase_date']
            item = request.form['item']
            description = request.form['description']
            category_name = request.form['category']
            quantity = request.form['quantity']
            unit_price = request.form['unit_price']
            amount = request.form['amount']

            expense = Expenses(purchase_date=purchase_date, item=item, description=description, category_id = category_name, quantity=quantity, unit_price=unit_price, amount=amount)
            db.session.add(expense)
            db.session.commit()
            return redirect("/viewexpense")
   
     return render_template('update.html', expense = expense)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    exp = Expenses.query.filter_by(id=id).first()
    if exp:
        db.session.delete(exp)
        db.session.commit()
        return redirect('/viewexpense')
    
    


