# import app variable from app package (this folder)
from app import app
from flask import render_template, flash, redirect
# import LoginForm class from the forms module (member of the app package)
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'renzo'}
    posts = [
        {
            'author': {'username': 'Aitana'},
            'body': "I want to see the animals!"
        },
        {
            'author': {'username': 'Abigail'},
            'body': "I'm researching for a place to live in Spain."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
