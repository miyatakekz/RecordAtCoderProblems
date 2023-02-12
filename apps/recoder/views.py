from apps.app import db
from apps.crud.models import User
from apps.recoder.models import UserProblem
from flask import Blueprint, render_template, request, redirect
import scraping_function
from flask_login import login_required, current_user

from apps.recoder.form import UploadImageForm

# staticの指定なし
recoder = Blueprint("recoder", __name__, template_folder="templates")


# recoderアプリケーションを使ってエンドポイント作成
@recoder.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        user_problems = (
            db.session.query(User, UserProblem)
            .join(UserProblem)
            .filter(User.id == UserProblem.user_id)
            .all()
        )
        # joinして一覧取得
        return render_template("recoder/index.html", user_problems=user_problems)
    else:
        INPUT_URL = request.form.get("problem_url")
        is_solved = bool(request.form.get("is_solved"))
        # URLルールベースでのタイトル作成
        t1 = INPUT_URL[-1]
        T = INPUT_URL[-8:-2]
        T = T.upper() + " " + t1.upper() + "問題"
        # スクレイピング
        genre = request.form.get("genre")
        due = request.form.get("due")
        Problem_Statement = scraping_function.get_text()
        new_post = UserProblem(
            user_id=current_user,
            problem_path=INPUT_URL,
            is_solved=is_solved,
            genre=genre,
            Problem_Statement=Problem_Statement,
            due=due,
        )
        # データベース保存：add->commit
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")


@recoder.route("/create")
@login_required
def create():
    form = UploadImageForm()
    return render_template("recoder/create.html", form=form)
