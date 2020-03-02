from flask import Blueprint, request, render_template, make_response, Response, redirect, url_for, session

day2 = Blueprint('day2', __name__)


@day2.route('/day2')
def handle_day2():
    return 'day2'


@day2.route('/day2/request/', methods=['GET', 'POST'])
def handle_request():
    print("value of request.args: ", request.args)
    print("typeof request.args: ", type(request.args))
    print("value of request.form: ", request.form)
    print("type of request.form: ", type(request.form))
    return 'request success'


@day2.route('/day2/response/', methods=['GET', 'POST'])
def handle_response():
    # return "response success"
    # return "response success", 200
    # return render_template('hello.html')
    # return Response('response success')
    # return make_response('response success', 200)
    return redirect(url_for('day2.handle_day2'))


@day2.route('/day2/cookie/login/', methods=['GET', 'POST'])
def handle_cookie_login():
    print("请求方法：: ", request.method)
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'linan' and password == '123':
            response = Response('登录成功！你好，%s!' % username)
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            return response
        else:
            return '登录失败!'
    else:
        return 'Method not supported'


@day2.route('/day2/session/login/', methods=['GET', 'POST'])
def handle_session_login():
    print("请求方法：: ", request.method)
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'linan' and password == '123':
            response = Response('登录成功！你好，%s!' % username)
            session['username'] = username
            return response
        else:
            return '登录失败!'
    else:
        return 'Method not supported'


@day2.route('/day2/cookie/index/')
def handle_cookie_index():
    username = request.cookies.get('username')
    return '%s, 欢迎回来！' % username


@day2.route('/day2/session/index/')
def handle_session_index():
    username = session.get('username')
    return '%s, 欢迎回来！' % username
