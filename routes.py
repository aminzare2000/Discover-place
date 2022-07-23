from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from calltest import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    data = get_journal_by_issn('0029-3970')
    return render_template('index.html', data = data)

# @app.route('/work/<url_id>/', methods=['GET'])
# def work(url_id = None):
#     if(url_id is None):
#         return redirect(url_for('index'))
    
#     return render_template('wqork.html')

@app.route('/work/<url_id>/<int:year>', methods=['GET'])
def work(url_id, year):
    # https://api.openalex.org/works?filter=institutions.country_code:fr|host_venue.issn:0957-1558
    data = get_works(url_id, year)
    return render_template('work.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
        