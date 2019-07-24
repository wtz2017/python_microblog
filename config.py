import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Flask-SQLAlchemy 插件从 SQLALCHEMY_DATABASE_URI 配置变量中获取应用的数据库的位置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # 设置数据发生变更之后是否发送信号给应用
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 错误通知邮件配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    # 支持翻译的语言
    LANGUAGES = ['en', 'es', 'zh', 'ja', 'ko']

    # 翻译用到的 KEY
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    # 搜索
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
	
    POSTS_PER_PAGE = 3
