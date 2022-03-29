from tokenize import Name
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Automarke(db.Model):
    __tablename__ = 'Automarke'

    MarkenID = db.Column(db.Integer, primary_key=True, unique=True)
    FirstName = db.Column(db.String(120))
    LastName = db.Column(db.String(120))
    CarName = db.Column(db.Text)
    description = db.Column(db.Text)
    dueDate = db.Column(db.Date)
    isDone = db.Column(db.Integer)

