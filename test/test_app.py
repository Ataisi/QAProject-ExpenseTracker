# Import the necessary modules
from urllib import response
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db 
from application.models import Expenses
from application.routes import add_expense

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # create a test db and create a new instance of the Expenses model
    def setUp(self):
        # Create db and the database table
        db.create_all()
        test_new_expense = Expenses(purchase_date='2022-10-09', item='Phone', description='Samsung S21',  quantity=2, unit_price=950.00, amount=1900, category_id = '1',)
        db.session.add(test_new_expense)
        db.session.commit()


    

""" 
Test to confirm that a new expense is added to the db
Given that an expense with Id=1 exits
When a new expense is added 
Then new expense id = 2 
"""

class TestAdd(TestBase):
    def test_add_expense(self):
        response = self.client.post( 
        url_for(add_expense),
        data = dict(purchase_date='2022-10-08', item='Book', description='Novel', quantity=1, unit_price=600.00, amount=600, category_id = '5',)
        )
        assert Expenses.query.filter_by(item="Book").id ==2

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestDelete(TestBase):
    def test_delete_expense(self):
        response = self.client.delete(
            '/delete/expense.id',
            data = dict(purchase_date='2022-10-09', item='Phone', description='Samsung S21',  quantity=2, unit_price=950.00, amount=1900, category_id = '1',)
        )
        assert len(Expenses.query.all()) == 0

    
    

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Expense', response.data)

    def test_addexpense(self):
        response = self.client.get(url_for('add_expense'))
        self.assertEqual(response.status_code, 200)

    def test_viewexpense(self):
        response = self.client.get(url_for('view_expense'))
        self.assertEqual(response.status_code, 200)