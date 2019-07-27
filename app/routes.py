from app import app
from flask import render_template

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