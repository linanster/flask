from flask import Blueprint

from App.models import mydb, User

blue1 = Blueprint('blue1', __name__)

@blue1.route('/blue1')
def handle_blue1():
    return 'blue1'

@blue1.route('/blue1/createdb/')
def createdb():
    mydb.create_all()
    return '数据库创建成功'

@blue1.route('/blue1/dropdb/')
def dropdb():
    mydb.drop_all()
    return '数据库删除成功'

@blue1.route('/blue1/adduser/')
def adduser():
    user1 = User()
    user1.username = 'user1'
    user1.age = 30
    user1.save()
    return '添加数据成功'