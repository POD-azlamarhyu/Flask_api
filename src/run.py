from app.main import app
from flask import Flask,render_template,jsonify

# from main 
from flask import Flask, render_template, jsonify
from app.models import db

from app.api import api

# Flask本体
app = Flask(__name__)

# ファイルから設定を読み込む
app.config.from_pyfile('./app/conf.cfg')

# DB初期化
db.init_app(app)

# Blueprint登録
app.register_blueprint(api)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': {
        'code': 'Not found',
        'message': 'Page not found.'
    }}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# if __name__ == "__main__":
#     try:
#         app.run(host="0.0.0.0",port=5000,debug=True)
#     except Exception:
#         print("surver error")