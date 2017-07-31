from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateForm(Form):
    info = StringField(validators=[DataRequired()])
