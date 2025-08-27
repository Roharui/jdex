
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .. import db

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    grade: Mapped[str] = mapped_column(String(10), nullable=False)
    class_name: Mapped[str] = mapped_column(String(50), nullable=False)
    student_id: Mapped[str] = mapped_column(String(20), nullable=False)
    point: Mapped[int] = mapped_column(Integer, default=0)


    def __repr__(self):
        return f'<User {self.email}>'
