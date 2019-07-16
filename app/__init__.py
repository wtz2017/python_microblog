from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
# 告知 Flask-Login 哪个视图函数用于处理登录认证，'login'值是登录视图函数（endpoint）名
login.login_view = 'login'

from app import routes, models
