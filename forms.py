from wtforms import Form, PasswordField, StringField


class LoginForm(Form):
    password = PasswordField('password')


class PostForm(Form):
    title = StringField('postTitle')
