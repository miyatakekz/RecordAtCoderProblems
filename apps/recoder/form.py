# from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField
from wtforms import URLField
from wtforms.validators import DataRequired, URL
from wtforms import BooleanField, StringField


class UploadImageForm(FlaskForm):
    # ファイルフィールドに必要なバリデーションを設定する
    # ユーザーフォームのusername属性のラベルとバリデータを設定する
    problem_path = URLField(
        "問題",
        validators=[DataRequired(), URL(message="URLの形式で入力してください。")],
    )
    is_solved = BooleanField("７日後リマインドしますか？")
    genre = StringField("タグ：全探索・ニブタン・DP・グラフ")
    # due = DateTimeField("復習日")
    # ユーザーフォームsubmitの文言を設定する
    submit = SubmitField("新規登録")


class Detail(FlaskForm):
    submit = SubmitField("問題文")


class DeleteForm(FlaskForm):
    submit = SubmitField("削除")


class UpdateForm_add(FlaskForm):
    submit = SubmitField("+3日")


class UpdateForm_sub(FlaskForm):
    submit = SubmitField("-2日")


class UpdateForm_done(FlaskForm):
    submit = SubmitField("done")
