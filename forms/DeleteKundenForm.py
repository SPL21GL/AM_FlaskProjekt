from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteKundenForm(FlaskForm):
    KundenID = HiddenField("KundenID")
