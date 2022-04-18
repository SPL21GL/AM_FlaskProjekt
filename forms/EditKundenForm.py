from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields import SelectField
from wtforms.fields.simple import StringField, TextAreaField, HiddenField

Führerscheinklasse = (
    ("AM", "AM"),
    ("A1", "A1"),
    ("A2", "A2"),
    ("A", "A"),
    ("B1", "B1"),
    ("B", "B"),
    ("C1", "C1"),
    ("C", "C"),
    ("D1", "D1"),
    ("D", "D"),
    ("BE", "BE"),
    ("C1E", "C1E"),
    ("CE", "CE"),
    ("D1E", "D1E"),
    ("DE", "DE"),
    ("F", "F"),
)

class editKundenForm(FlaskForm):
    KundenID = HiddenField("KundenID")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Geburtstag = DateField("Geburtstag")
    Wohnohrt = TextAreaField("Wohnort")
    Fuehrerscheinklasse = SelectField("Fuehrerscheinklasse", choices = Führerscheinklasse, default = 'B1')