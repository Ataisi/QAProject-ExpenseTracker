from application import db 
import datetime

# defining the tables  in  the database
class Category(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), nullable=False, unique = True)
    expenses = db.relationship('Expenses', backref='category')

class Expenses (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.String(12), nullable = False)
    item = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    #category_name = db.Column(db.String(50), nullable=True)
    quantity = db.Column(db.Integer, nullable = False)
    unit_price = db.Column(db.Float, nullable = True)
    amount = db.Column(db.Float, nullable = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)