from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms.fields import SelectField
from wtforms import validators
from wtforms.fields import DecimalField


YEAR_CHOICES = (
    ("1990", "1990"),
    ("1995", "1995"),
    ("2000", "2000"),
    ("2005", "2005"),
    ("2010", "2010"),
    ("2015", "2015"),
    ("2020", "2020"),
    ("2022", "2022"),
)


FARBE = (
    ("Blau", "Blau"),
    ("Rot", "Rot"),
    ("Grün", "Grün"),
    ("Schwarz", "Schwarz"),
    ("Silber", "Silber"),
)


class AddMietwagen(FlaskForm):
    Farbe = SelectField("Farbe", choices=FARBE, default='Blau')
    kmStand = DecimalField("kmStand", validators = [validators.InputRequired()])
    Leistung = DecimalField("Leistung", validators = [validators.InputRequired()])
    Erstzulasung = DateField("Erstzulassung")
    Kennzeichen = StringField("Kennzeichen", validators = [validators.InputRequired()])
    Baujahr = SelectField("Baujahr", choices=YEAR_CHOICES, default='2022')
