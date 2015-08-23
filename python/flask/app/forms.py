from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Required, EqualTo

class LoginForm(Form):
    user_id = StringField("User ID", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    remember_me = BooleanField('remember me', default = False)

class RegisterForm(Form):
    user_id = StringField("User ID", [DataRequired()])
    pass_valid = [Required()]
    pass_valid.append(EqualTo('confirm', message = 'Passwords must match'))
    password = PasswordField('New Password', pass_valid)
    confirm = PasswordField('Repeat Password')
    
