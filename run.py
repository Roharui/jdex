from app import app, db

from app.models import User # User 모델 임포트

with app.app_context():
    # 데이터베이스 스키마 생성
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)