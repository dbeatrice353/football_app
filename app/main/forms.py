from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, BooleanField, TextField, PasswordField, validators, SelectField
from flask.ext.pagedown.fields import PageDownField
from wtforms.validators import Required


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    first_name = TextField('First Name', [validators.Length(min=4, max=25)])
    last_name = TextField('Last Name', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=4, max=45)])
    password_ = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])
    submit = SubmitField('Submit')

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    password_ = PasswordField('Password', [validators.Required()])
    submit = SubmitField('Submit')
