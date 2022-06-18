from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms.fields import SelectField
from wtforms import validators

FÜHRERSCHEINKLASSE = (
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


class AddKundenForm(FlaskForm):
    Vorname = StringField("Vorname", validators = [validators.InputRequired()])
    Nachname = StringField("Nachname", validators = [validators.InputRequired()])
    Geburtstag = DateField("Geburtstag")
    Wohnort = StringField("Wohnort")
    Fuehrerscheinklasse = SelectField(
        "Fuehrerscheinklasse", choices=FÜHRERSCHEINKLASSE, default='B1')
