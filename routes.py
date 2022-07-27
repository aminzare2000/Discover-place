from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from calltest import *

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
@app.route('/index', methods=['GET' , 'POST'])
def index():
    # 1611-3349
    # 0029-3970


    if request.method == 'GET':
        venues = get_journal_by_issn('1611-3349')
        return render_template('index.html', venues = venues)
    else:
        issn = request.form['issn']
        venues = get_journal_by_issn(issn)
        return render_template('index.html', venues = venues)



# @app.route('/work/<url_id>/', methods=['GET'])
# def work(url_id = None):
#     if(url_id is None):
#         return redirect(url_for('index'))
    
#     return render_template('wqork.html')

@app.route('/work/<url_id>/<int:year>', methods=['GET'])
@app.route('/work/<url_id>/<int:year>/<int:page>', methods=['GET'])
def work(url_id, year , page = None):
    # https://api.openalex.org/works?filter=institutions.country_code:fr|host_venue.issn:0957-1558
    works_pi , pages = get_works(url_id, year,page)
    return render_template('work.html', works = works_pi,        
                                        pages=pages , 
                                        year=year , 
                                        url_id=url_id)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
        