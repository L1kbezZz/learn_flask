from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Roman'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was cool!'
        },
        {
            'author': {'username': 'Miguel'},
            'body': 'The best Flask tutorial here!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)