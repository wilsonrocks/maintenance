from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class CreateForm(FlaskForm):
    info = StringField("info", validators=[DataRequired()])
    room = SelectField("room",coerce=int)
    category = SelectField("category", coerce=int)
