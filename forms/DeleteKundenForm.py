from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField
from wtforms.fields.simple import StringField


class DeleteKunden(FlaskForm):
    KundenID = StringField("KundenID")
