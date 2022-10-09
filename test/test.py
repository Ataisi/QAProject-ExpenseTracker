# Import the necessary modules
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from app import app, db, Register

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

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()

        # Create test expense
        test_new_expense = Expenses(purchase_date='2022-10-09', item='Phone', description='Samsung S21', category_id = 'Appliances', quantity=2, unit_price=950.00, amount=1900)

        # save users to database
        db.session.add(test_new_expense)
        db.session.commit()


class TestDelete(TestBase):
    def test_delete_expense(self):
        # delete Chewbarka from the database
        response = self.client.delete(
            url_for('delete_***'),
            data = dict(item="Phone")
        )
        # query the dog table - if Chewbarka has been deleted,
        # the query should return an empty list
        assert len(Expenses.query.all()) == 0

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MsWoman', response.data)

    def test_home_addexpense(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)