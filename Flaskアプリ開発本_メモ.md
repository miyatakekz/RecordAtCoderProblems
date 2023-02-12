# アプリ作成手順・メモ
## 環境作成
$ python3 -m venv venv
$ source venv/bin/activate

## パッケージインストール
---
(venv) $ pip install -r requirements.txt
---
## 基本
- 1app.py作成
- 2環境変数の設定
    <!-- - 下記コマンド逐次実行
        - export FLASK_APP=app.py
        - export FLASK_ENV=development -->
    - .env作成
        - python-dotenvパッケージ使用
            - pip install python dotenv
            - mkdir apps/.env

- 3ルーティング確認
    - flask routes
- ブループリント
    - apps/sample
        - Blueprint(sanmple, __name__, template_folder="templates")

## 見た目
- bootsrapダウンロード４章参照

## データベース作成
- flask db migrate
- flask db upgrade
## リレーション
- flask shell
    - >>> from apps.app import db
    - from apps.crud.models import User
    - from apps.recoder.models import UserProblem
- innner join
    - db.session.query( User, UserProblem).join( UserProblem ).filter( User.id == UserProblem.user_id).all()
- オブジェクト取得