from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
# データベースと秘密鍵の設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///satonaka.db'
app.config['SECRET_KEY'] = 'satonakahiromu'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
 #ユーザモデル定義
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)  # メールアドレス
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(15), nullable=False)  # 投稿者名の追加
    role = db.Column(db.String(10), nullable=False)  # 役割の追加（admin か poster）

# ユーザーローダーの設定
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ホームページへのアクセスをログインページへリダイレクト
@app.route('/')
def redirect_to_login():
    return redirect(url_for('login'))

#ユーザー登録機能
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        role = request.form['role']

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(email=email, username=username, password=hashed_password, name=name, role=role)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html')

# ログインページ
# ログインページ
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # ユーザー名からメールアドレスへ変更
        password = request.form['password']
        user = User.query.filter_by(email=email).first()  # username を email に変更
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Login Failed'
    return render_template('login.html')

# ダッシュボード（認証後のページ）
@app.route('/dashboard')
@login_required
def dashboard():
    return 'Welcome to the Dashboard'

# ログアウト
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# データベースの作成
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)