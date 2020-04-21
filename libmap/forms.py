from wtforms import Form, BooleanField, StringField, PasswordField, validators,DateField

class SearchForm(Form):
    start_date = StringField('Start Date')
    end_date = StringField('End Date')
    title = StringField('Author')