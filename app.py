from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.secret_key = 'secret'
db = SQLAlchemy(app)

# Khai báo model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

# Tạo giao diện admin
admin = Admin(app, name="Quản lý thư viên", template_mode="bootstrap3")
admin.add_view(ModelView(Book, db.session))
admin.add_view(ModelView(User, db.session))

# Thêm route chính trang chủ
@app.route('/')
def index():
    return '<h1>Chào mừng đến với hệ thống quản lý thư viện!</h1><p> Truy cập <a href="/admin">/admin</a> để vào trang quản trị.</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)