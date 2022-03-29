from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms import validators

class AddAutoForm(FlaskForm):
    FirstName = StringField("FirstName", validators = [validators.InputRequired()])
    LastName  = StringField("LastName", validators = [validators.InputRequired()])
    CarName = StringField("CarName")
    description = TextAreaField("description", validators = [validators.InputRequired()])
    dueDate = DateField("dueDate")
    isDone = BooleanField("isDone")