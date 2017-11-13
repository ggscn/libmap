from flask import Flask,render_template,request
from flask_googlemaps import GoogleMaps, Map
from wtforms import Form, BooleanField, StringField, PasswordField, validators,DateField

from util import bigquery

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)
GoogleMaps(app)

class SearchForm(Form):
    start_date = StringField('Start Date')
    end_date = StringField('End Date' )
    title = StringField('Author')

@app.route('/', methods=['GET', 'POST'])
def home():
    markers = []
    form = SearchForm(request.form)
    if request.method == 'GET':
        mymap = Map(
            identifier="view-side",
            lat=37.4419,
            lng=-122.1419,
            markers=(1,1)
            )
        return render_template('home.html', form=form, mymap=mymap)

    elif request.method == 'POST' and form.validate():
        params = {}
        params['table_address'] = 'gdelt-bq:hathitrustbooks'
        params['start_date'] = form.start_date.data
        params['end_date'] = form.end_date.data
        params['title'] = form.title.data
        locations = bigquery.query(**params)
        for location in locations:
            lat = location[0]
            lon = location[1]
            marker = (lat,lon)
            print(marker)
            markers.append(marker)
        mymap = Map(
            identifier="view-side",
            lat=37.4419,
            lng=-122.1419,
            markers=markers,
            zoom=5
            )
        return render_template('home.html', form=form, mymap=mymap)
     
    
