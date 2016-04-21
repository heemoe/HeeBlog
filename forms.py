from wtforms import Form,PasswordField,TextField,TextAreaField

class LoginForm(Form):
    password = PasswordField('password')


class PostForm(Form):
    title = TextField('postTitle')