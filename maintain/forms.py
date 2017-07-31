from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class CreateForm(Form):
    info = StringField("info", validators=[DataRequired()])
    room = SelectField("room", validators=[DataRequired()])
    category = SelectField("category", validators=[DataRequired()])
