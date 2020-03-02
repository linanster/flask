from flask import Blueprint

blue2 = Blueprint('blue2', __name__)

@blue2.route('/blue2')
def handle_blue2():
    return 'blue2'