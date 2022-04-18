from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.fields import SelectField
from wtforms import validators

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


class AddKundenForm(FlaskForm):
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Geburtstag = DateField("Geburtstag")
    Wohnohrt = TextAreaField("Wohnort")
    Fuehrerscheinklasse = SelectField("Fuehrerscheinklasse", choices = Führerscheinklasse, default = 'B1')

#addKundenFormObject = AddKundenForm()


class AddAutoForm(FlaskForm):
    JaehrlicherUmsatz = StringField("JaehrlicherUmsatz")
    Gruendungsdatum  = SelectField("Gruendungsdatum", choices = YEAR_CHOICES, default = '2022' )
    MarkenName = StringField("MarkenName")
    VerkaufszahlenProJahr = StringField("VerkaufszahlenProJahr")
    Herststellland = StringField("Herststellland")

class AddMietwagen(FlaskForm):
    Farbe = SelectField("Farbe")
    kmStand = TextAreaField("kmStand")
    Leistung = TextAreaField("Leistung")
    Erstzulasung = DateField("Erstzulassung")
    Kennzeichen = TextAreaField("Kennzeichen")
    Baujahr = SelectField("Baujahr", choices = YEAR_CHOICES, default = '2022')

#addAutoFormObject = AddAutoForm()

#validators = [validators.InputRequired()]