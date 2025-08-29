import os

from flask import render_template, request, session, redirect

from .. import app, db, bcrypt
from ..models.users import User

from ..utils.mail import send_email

def password_hash_fn(password: str) -> str:
    return bcrypt.generate_password_hash(password).decode('utf-8')

@app.route('/login', methods=['GET'])
def login_form():
    if session.get('user_id'):
        return redirect('/')

    return render_template('login.html')

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
        return '<script>alert("로그인에 실패했습니다.");location.href="/login"</script>', 401

    session['user_id'] = user.id

    return f'ID: {user.id}, Username: {user.name}, Email: {user.email}'


# 회원가입

@app.route('/register', methods=['GET'])
def register_form():
    if session.get('user_id'):
        return redirect('/')
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']

    existing_user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    if existing_user is None:
        return 'This User is Not allowed', 400
    
    if len(existing_user.password_hash) > 0:
        return 'This User is Not allowed', 400

    link = f"http://{os.getenv('HOSTNAME')}/pw/{existing_user.uuid}"

    send_email(email, f"비밀번호 재설정 이메일입니다 : {link}")

    return f'Email has Sent, Please Send Email: {email}'

# 비밀번호 세팅/재설정

@app.route('/pw/<uuid>', methods=['GET'])
def reset_pw_form(uuid):
    user = db.session.execute(db.select(User).filter_by(uuid=uuid)).scalar_one_or_none()

    if user is None:
        return 'User not found', 404

    if len(user.password_hash) > 0:
        return 'This User is Not allowed', 400
    
    return render_template('reset_pw.html', email=user.email, name=user.name, uuid=uuid)

@app.route('/pw/<uuid>', methods=['POST'])
def reset_pw(uuid): 
    new_password = request.form['new_password']

    user = db.session.execute(db.select(User).filter_by(uuid=uuid)).scalar_one_or_none()

    if user is None:
        return 'User not found', 404

    user.password_hash = password_hash_fn(new_password)
    db.session.commit()

    return 'Password reset successfully'