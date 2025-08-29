from flask import render_template, session, redirect

from .. import app, db
from ..models.users import User

@app.route('/')
def home():
    if not session.get('user_id'):
        return redirect('/login')
    user = db.session.execute(db.select(User).filter_by(id=session.get('user_id'))).scalar_one_or_none()
    return render_template('index.html', point=user.point)

@app.route('/about')
def about():
    users = User.query.all()
    return '<br>'.join([f'ID: {user.id}, Username: {user.username}, Email: {user.email}' for user in users])