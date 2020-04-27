from wtforms import Form, StringField

class SearchForm(Form):
    title = StringField('Title')
    author = StringField('Author')