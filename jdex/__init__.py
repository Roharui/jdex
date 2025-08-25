from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite 데이터베이스 설정. my_project 디렉터리에 'site.db' 파일 생성
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy 인스턴스 생성
db = SQLAlchemy(app)

from . import views, models