from wtforms import Form, BooleanField, StringField, PasswordField, validators,DateField

class SearchForm(Form):
    title = StringField('Title')
    author = StringField('Author')