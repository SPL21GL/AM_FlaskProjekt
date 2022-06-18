from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteMietwagen(FlaskForm):
    AutoID = HiddenField("AutoID")
