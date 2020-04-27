from flask import Flask, render_template, request, jsonify

from .forms import SearchForm
from .util.bigquery import BigQuery

app = Flask(__name__, instance_relative_config=True, template_folder='templates')


@app.route('/', methods=['GET'])
def home():
    form = SearchForm(request.form)
    if request.method == 'GET':
        return render_template('home.html', form=form)
    

@app.route('/query', methods=['GET'])
def query():
    """Handle a GET request to return the locations of an author or title
    as a list of dicts"""

    author = request.args.get('author', '')
    title = request.args.get('title', '')

    query_str_template = BigQuery.get_query_str(
        'coords_by_author_title')
    rows = BigQuery().query(query_str_template.format(
        title=title, author=author))
    return jsonify({'data':rows})