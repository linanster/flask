from flask import Flask
from App.ext import init_ext
from App.settings import envs
from App.views import init_views


def create_app(env):
    app = Flask(__name__)
    # uri格式： 数据库+驱动://用户名:密码@主机:端口/库名
    # MYSQL: mysql+pymysql://root:123456@localhost:3306/testdb
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(envs.get(env))

    init_ext(app)
    init_views(app)
    return app