from flask import Flask, render_template, request, jsonify

from .forms import SearchForm
from .util import bigquery

app = Flask(__name__, instance_relative_config=True, template_folder='templates')
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)
app.run(debug=True)


@app.route('/', methods=['GET'])
def home():
    form = SearchForm(request.form)
    if request.method == 'GET':
        return render_template('home.html', form=form)
    

@app.route('/query', methods=['GET'])
def query():
    return jsonify({'test':'test'})