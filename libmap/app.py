from flask import Flask,render_template

from libmap.lib import bigquery


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)

@app.route("/")
def home():
    bigquery.get_credentials()
    return render_template('home.html')