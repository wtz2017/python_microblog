import os
from config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler


# app 包由 app 目录和 __init__.py 脚本来定义构成，并在 from app import routes 语句中被引用。
# app 变量被定义为 __init__.py 脚本中的 Flask 类的一个实例，以至于它成为 app 包的属性。
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
# 告知 Flask-Login 哪个视图函数用于处理登录认证，'login'值是登录视图函数（endpoint）名
login.login_view = 'login'

mail = Mail(app)

bootstrap = Bootstrap(app)

moment = Moment(app)

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    # 将日志文件的大小限制为10KB，并只保留最后的十个日志文件作为备份
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    # 服务器每次启动时都会在日志中写入如下一行，以便统计服务器何时重新启动过。
    app.logger.info('Microblog startup')

# routes 等模块是在底部导入的，而不是在脚本的顶部。
# 最下面的导入是解决循环导入的问题，这是 Flask 应用程序的常见问题。
# 你将会看到 routes 模块需要导入在这个脚本中定义的 app 变量，
# 因此将 routes 的导入放在底部可以避免由于这两个文件之间的相互引用而导致的错误。
from app import routes, models, errors
