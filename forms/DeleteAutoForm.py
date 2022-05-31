from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteAuto(FlaskForm):
    KundenID = HiddenField("KundenID")