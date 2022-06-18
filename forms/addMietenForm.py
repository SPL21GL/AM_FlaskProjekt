from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms.fields import SelectField
from wtforms import validators
from wtforms.fields import DecimalField


YEAR_CHOICES = (
    ("1990", "1990"),
    ("1991", "1991"),
    ("1992", "1992"),
    ("1993", "1993"),
    ("1994", "1994"),
    ("1995", "1995"),
    ("1996", "1996"),
    ("1997", "1997"),
    ("1998", "1998"),
    ("1999", "1999"),
    ("2000", "2000"),
    ("2001", "2001"),
    ("2002", "2002"),
    ("2003", "2003"),
    ("2004", "2004"),
    ("2005", "2005"),
    ("2006", "2006"),
    ("2007", "2007"),
    ("2008", "2008"),
    ("2009", "2009"),
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    ("2014", "2014"),
    ("2015", "2015"),
    ("2016", "2016"),
    ("2017", "2017"),
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021"),
    ("2022", "2022"),
)


class AddMietwagen(FlaskForm):
    Farbe = StringField("Farbe")
    kmStand = DecimalField("kmStand", validators=[validators.InputRequired()])
    Leistung = DecimalField("Leistung", validators=[
                            validators.InputRequired()])
    Erstzulasung = DateField("Erstzulassung")
    Kennzeichen = StringField("Kennzeichen", validators=[
                              validators.InputRequired()])
    Baujahr = SelectField("Baujahr", choices=YEAR_CHOICES, default='2022')
