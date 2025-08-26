from flask import Flask
from flask_bcrypt import Bcrypt

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
bcrypt = Bcrypt(app)

# 세션 관리를 위한 비밀 키 설정
app.config['SECRET_KEY'] = 'your_secret_key'  

# SQLite 데이터베이스 설정. my_project 디렉터리에 'site.db' 파일 생성
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Base(DeclarativeBase):
    pass

# SQLAlchemy 인스턴스 생성
db = SQLAlchemy(app, model_class=Base)

from . import views, models
