from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.models import User, Recipe

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jillian'}
    recipes = [
        {
            'name' : 'Chilli Chicken',
            'ingredients' : [
                ('Spring Onion', 1),
                ('Baby Corn', 1)
            ]
        },
        {
            'name' : 'Stir Fry',
            'ingredients' : [
                ('Onion', 1),
                ('Baby Corn', 1)
            ]
        }
    ]

    return render_template('index.html', title='Home', user=user, recipes=recipes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)