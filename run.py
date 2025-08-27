from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

from app import app, db

from app.models import *

with app.app_context():
    # 데이터베이스 스키마 생성
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)