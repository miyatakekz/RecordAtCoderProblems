# レコードリマインダー for atc
## アプリ概要
競技プログラミングサイト「AtCoder」の問題記録/復習アプリ。

問題の記録（スクレイピング）と解けなかった問題をリマインドする機能（todoリスト）。
## 実行環境の作成
### Git Clone

```
$ git clone https://github.com/ml-flaskbook/flaskbook.git
```

### 環境作成
```
$ python3 -m venv venv
$ source venv/bin/activate
```
### パッケージインストール
```
(venv) $ pip install -r requirements.txt
```

### データベース作成
```
$ flask db init
$ flask db migrate
$ flask db upgrade
```
## アプリケーション起動

```
(venv) $ flask run
```