from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
# データベースと秘密鍵の設定_将来的にここは開発が終わったら固定値だとまずい
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sap.db'
app.config['SECRET_KEY'] = 'sappy'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# ユーザモデルテー偽
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# ユーザーローダーの定義
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))