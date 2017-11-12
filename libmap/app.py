from flask import Flask,render_template

from libmap.lib import bigquery


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)

@app.route("/")
def home():
    params = {}
    params['table_address'] = 'gdelt-bq:internetarchivebooks'
    params['start_date'] = '1800'
    params['end_date'] = '1850'
    params['author'] = 'Herman Melville'
    
    bigquery.query(**params)
    return render_template('home.html')