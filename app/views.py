__author__ = 'idclark'
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'ian'}
    posts = [
        {'author': {'nickname':'jon'},
        'body': 'nice day today'},
        {'author': {'nickname':'fred'},
         'body': 'it\'s raining in baltimore'}]
    return render_template("index.html", title='Home',
                           user=user, posts=posts)
