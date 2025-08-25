from flask import render_template

from .. import app
from ..models.users import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    users = User.query.all()
    return '<br>'.join([f'ID: {user.id}, Username: {user.username}, Email: {user.email}' for user in users])