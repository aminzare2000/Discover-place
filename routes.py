from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from calltest import get_journal_by_issn

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    data = get_journal_by_issn('0029-3970')
    return render_template('index.html', data = data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
        