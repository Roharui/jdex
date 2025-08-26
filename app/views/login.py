
from flask import render_template, request, session, redirect

from .. import app, db, bcrypt
from ..models.users import User

def password_hash_fn(password: str) -> str:
    return bcrypt.generate_password_hash(password).decode('utf-8')

@app.route('/login', methods=['GET'])
def login_form():
    if session.get('user_id'):
        return redirect('/')

    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register_form():
    if session.get('user_id'):
        return redirect('/')
    return render_template('register.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return 'Logged out successfully'

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    if user is None or bcrypt.check_password_hash(user.password_hash, password) is False:
        return 'Invalid email or password', 401

    session['user_id'] = user.id

    return f'ID: {user.id}, Username: {user.name}, Email: {user.email}'

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    grade = request.form['grade']
    class_name = request.form['class_name']
    student_id = request.form['student_id']
    password_hash = password_hash_fn(request.form['password'])

    existing_user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    if existing_user is not None:
        return 'Email already registered', 400

    new_user = User(name=name, email=email, grade=grade, class_name=class_name, student_id=student_id, password_hash=password_hash) # type: ignore
    db.session.add(new_user)
    db.session.commit()

    return f'User {new_user.name} registered successfully with ID {new_user.id}'
