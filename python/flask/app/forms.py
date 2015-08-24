from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Required, EqualTo

class AddComicForm(Form):
    pass