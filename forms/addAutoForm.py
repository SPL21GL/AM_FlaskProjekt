from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import SelectField
from wtforms import validators
from wtforms.fields import DecimalField

Gruendungsdatum_CHOICES = (
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
    JaehrlicherUmsatz = DecimalField("JaehrlicherUmsatz", validators = [validators.InputRequired()])
    Gruendungsjahr = SelectField(
        "Gruendungsjahr", choices=Gruendungsdatum_CHOICES, default='2022')
    MarkenName = StringField("MarkenName")
    VerkaufszahlenProJahr = DecimalField("VerkaufszahlenProJahr", validators = [validators.InputRequired()])
    Herststellland = StringField("Herststellland", validators = [validators.InputRequired()])
