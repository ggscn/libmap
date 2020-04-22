from flask import Flask, render_template, request, jsonify

from .forms import SearchForm
from .util.bigquery import BigQuery

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
    author = request.args.get('author', '')
    title = request.args.get('title', '')
    print(author, title)

    query_str_template = BigQuery.get_query_str(
        'coords_by_author_title')
    rows = BigQuery().query(query_str_template.format(
        title=title, author=author))
    return jsonify({'data':rows})