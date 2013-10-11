__author__ = 'idclark'
from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID=' + form.openid.data +
              'remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In',
                           form=form,
                           providers = app.config['OPENID_PROVIDERS'])



