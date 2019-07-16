from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # 新的 posts 字段，用 db.relationship 初始化。这不是实际的数据库字段，而是用户和其动态之间关系的高级视图，
    # 因此它不在数据库图表中。对于一对多关系，db.relationship 字段通常在“一”的这边定义，并用作访问“多”的便捷方式。
    # backref 参数定义了代表“多”的类的实例反向调用“一”的时候的属性名称
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 本处的 user 是数据库表的名称，Flask-SQLAlchemy 自动设置类名为小写来作为对应表的名称
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
