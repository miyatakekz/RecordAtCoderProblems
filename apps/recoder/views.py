from apps.app import db
from apps.crud.models import User
from apps.recoder.models import UserProblem
from flask import Blueprint, render_template, redirect, url_for
import fn_scraping
from flask_login import login_required, current_user
from datetime import datetime, timedelta, date

from apps.recoder.form import (
    UploadImageForm,
    DeleteForm,
    Detail,
    UpdateForm_add,
    UpdateForm_sub,
    UpdateForm_done,
)

import re


# staticの指定なし
recoder = Blueprint("recoder", __name__, template_folder="templates")


# recoderアプリケーションを使ってエンドポイント作成
@recoder.route("/")
def index():
    user_problems = (
        db.session.query(User, UserProblem)
        .join(UserProblem)
        .filter(User.id == UserProblem.user_id)
        .order_by(UserProblem.due)
        .all()
    )
    # joinして一覧取得
    delete_form = DeleteForm()
    detail_form = Detail()
    update_form_add = UpdateForm_add()
    update_form_sub = UpdateForm_sub()
    update_form_done = UpdateForm_done()
    return render_template(
        "recoder/index.html",
        user_problems=user_problems,
        delete_form=delete_form,
        detail_form=detail_form,
        update_form_add=update_form_add,
        update_form_sub=update_form_sub,
        update_form_done=update_form_done,
        kon=date.today(),
    )


@recoder.route("/create", methods=["GET", "POST"])
@login_required
def create():
    # UserFormをインスタンス化する
    form = UploadImageForm()
    # フォームの値をバリデートする
    # if form.validate_on_submit():
    if form.validate():
        # ユーザーを作成する
        INPUT_URL = form.problem_path.data
        genre = form.genre.data
        # is_solved = bool(form.is_solved.data)
        # URLルールベースでのタイトル作成
        # t1 = INPUT_URL[-1]
        T = INPUT_URL[-8:-2]
        T = T.upper() + " コンテスト"  # " + t1.upper() + "問題"
        # スクレイピング
        # genre = "テスト全探索"
        # due = form.due.data
        due = datetime.now() + timedelta(days=7)
        Problem_Statement, Problem_Title_str = fn_scraping.get_protext(INPUT_URL)
        # 正規表現
        Problem_Title_str = re.sub("'\n'", "", Problem_Title_str)
        Problem_Statement = re.sub("'\n'", "", Problem_Statement)
        Problem_Title_str = re.sub(r"()", "", Problem_Title_str)
        Problem_Statement = re.sub(r"()", "", Problem_Statement)
        Problem_Statement = Problem_Statement[5:]
        Problem_Title = T
        new_post = UserProblem(
            user_id=current_user.id,
            problem_path=INPUT_URL,
            is_solved=form.is_solved.data,
            genre=genre,
            Problem_Title=Problem_Title,
            Problem_Statement=Problem_Statement,
            Problem_Title_str=Problem_Title_str,
            due=due,
        )
        # ユーザーを追加してコミットする
        db.session.add(new_post)
        db.session.commit()
        # ユーザーの一覧画面へリダイレクトする
        return redirect(url_for("recoder.index"))
    return render_template("recoder/create.html", form=form)


@recoder.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    post = UserProblem.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("recoder.index"))


@recoder.route("/detail/<int:id>", methods=["POST"])
@login_required
def detail(id):
    post = UserProblem.query.get(id)
    return render_template("recoder/detail.html", post=post)


@recoder.route("/update_add/<int:id>", methods=["POST"])
@login_required
def update_add(id):
    # UserFormをインスタンス化する
    post = UserProblem.query.get(id)
    # post.Problem_Title_str = request.form.get("Problem_Title_str")
    post.due = post.due + timedelta(days=3)

    db.session.commit()
    return redirect(url_for("recoder.index"))


@recoder.route("/update_sub/<int:id>", methods=["POST"])
@login_required
def update_sub(id):
    # UserFormをインスタンス化する
    post = UserProblem.query.get(id)
    # post.Problem_Title_str = request.form.get("Problem_Title_str")
    post.due = post.due - timedelta(days=2)

    db.session.commit()
    return redirect(url_for("recoder.index"))


@recoder.route("/update_done/<int:id>", methods=["POST"])
@login_required
def update_done(id):
    # UserFormをインスタンス化する
    post = UserProblem.query.get(id)
    # post.Problem_Title_str = request.form.get("Problem_Title_str")
    post.is_solved = 1 - post.is_solved

    db.session.commit()
    return redirect(url_for("recoder.index"))
