from flask import Flask

# Flaskクラスインスタンス化
app = Flask(__name__)


# 2023/02/12久しぶり
@app.route("/")
def index():
    return "test page, Helloooooo!"
