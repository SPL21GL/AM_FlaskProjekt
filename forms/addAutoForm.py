from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import SelectField

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
    JaehrlicherUmsatz = StringField("JaehrlicherUmsatz")
    Gruendungsdatum = SelectField(
        "Gruendungsdatum", choices=Gruendungsdatum_CHOICES, default='2022')
    MarkenName = StringField("MarkenName")
    VerkaufszahlenProJahr = StringField("VerkaufszahlenProJahr")
    Herststellland = StringField("Herststellland")
