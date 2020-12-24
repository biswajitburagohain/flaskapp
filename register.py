from wtforms import Form, StringField, TextAreaField, PasswordField, validators

class RegisterForm(Form):
    name = StringField('Name', validators=[validators.input_required(), validators.length(min=1, max=100)])
    username =StringField('UserName', validators=[validators.length(min=1, max=40), validators.input_required()])
    email = StringField('Email ID', validators=[validators.length(min=6, max=50)])
    password = PasswordField('Password ', validators=[validators.DataRequired(), 
                                                  validators.equal_to('confirm', message='Password does not match')])
    confirm= PasswordField('Confirm Password')

class Login(Form):
    username = StringField('User Name', validators=[validators.input_required()])
    password = PasswordField('Password', validators=[validators.DataRequired("Password")])