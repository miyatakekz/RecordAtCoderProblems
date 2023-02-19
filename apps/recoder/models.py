from datetime import datetime
from apps.app import db


class UserProblem(db.Model):
    __tablename__ = "user_problems"
    id = db.Column(db.Integer, primary_key=True)
    # ユーザーidをリレーション
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    problem_path = db.Column(db.String)
    is_solved = db.Column(db.Boolean, default=False)
    # add
    Problem_Title = db.Column(db.String)
    Problem_Title_str = db.Column(db.String)
    Problem_Statement = db.Column(db.String)
    due = db.Column(db.DateTime, default=datetime.now())
    genre = db.Column(db.String)
    # データベース登録日時
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
