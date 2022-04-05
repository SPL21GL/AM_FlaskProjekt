from datetime import date
from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import SelectField
from wtforms.fields.core import Field
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


class AddAutoForm(FlaskForm):
    JaehrlicherUmsatz = StringField("JaehrlicherUmsatz")
    Gruendungsdatum  = SelectField("Gruendungsdatum", validators = [validators.InputRequired()], choices = YEAR_CHOICES, default = '2022' )
    MarkenName = StringField("MarkenName")
    VerkaufszahlenProJahr = DateField("VerkaufszahlenProJahr", validators = [validators.InputRequired()])
    Herststellland = StringField("Herststellland")