from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
import wtforms.validators

class LoginForm(Form):
    user_id = StringField("User ID", validators = [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()]
    remember_me = BooleanField('remember me', default = False)

class RegisterForm(Form):
    user_id = StringField("User ID", [validators.DataRequired()])
    pass_valid = [validators.Required()]
    pass_valid[1] = validators.EqualTo('confirm', message = 'Passwords must match')]
    password = PasswordField('New Password', pass_valid)
    confirm = PasswordField('Repeat Password')
    
