from flask import Blueprint

from App.models import mydb

blue1 = Blueprint('blue1', __name__)

@blue1.route('/blue1')
def handle_blue1():
    return 'blue1'

@blue1.route('/blue1/createdb/')
def createdb():
    mydb.create_all()
    return '数据库创建成功'