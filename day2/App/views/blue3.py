from flask import Blueprint

blue3 = Blueprint('blue3', __name__)

@blue3.route('/blue3')
def handle_blue3():
    return 'blue3'