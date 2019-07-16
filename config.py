import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Flask-SQLAlchemy 插件从 SQLALCHEMY_DATABASE_URI 配置变量中获取应用的数据库的位置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # 设置数据发生变更之后是否发送信号给应用
    SQLALCHEMY_TRACK_MODIFICATIONS = False