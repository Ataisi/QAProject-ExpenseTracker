from sqlalchemy import Integer
from flask_wtf import Flask
from wtforms import StringField, SubmitField, HiddenField, SelectField, FloatField, HiddenField, IntegerField
from wtforms.fields.html5 import  DateField
from wtforms.validators import DataRequired, Length, ValidationError

class AddExpenseForm(FlaskForm):
    purchase_date = DateField('Purchase Date')
    item = StringField ('Item')
    description = StringField('Description')
    quantity = IntegerField('Quantity')
    unit_price = FloatField('Unit Price')
    amount = FloatField('amount')
    submit = SubmitField('Add Expense')
