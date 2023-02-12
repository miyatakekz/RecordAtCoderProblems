from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField
from wtforms import StringField


class UploadImageForm(FlaskForm):
    # ファイルフィールドに必要なバリデーションを設定する
    # ユーザーフォームのusername属性のラベルとバリデータを設定する
    problem_path = StringField(
        "問題URL",
        # validators=[
        #     DataRequired(message="ユーザー名は必須です。"),
        #     length(max=30, message="30文字以内で入力してください。"),
        # ],
    )
    # ユーザーフォームsubmitの文言を設定する
    submit = SubmitField("新規登録")


class DetectorForm(FlaskForm):
    submit = SubmitField("検知")


class DeleteForm(FlaskForm):
    submit = SubmitField("削除")
