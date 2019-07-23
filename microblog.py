from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


# 以下便于在 shell 中测试：
# app.shell_context_processor 装饰器将该函数注册为一个shell上下文函数。 
# 当flask shell命令运行时，它会调用这个函数并在shell会话中注册它返回的项目。
# 在添加shell上下文处理器函数后，你无需导入就可以通过 flask shell 使用数据库实例。
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}