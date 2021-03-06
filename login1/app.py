#! /usr/bin/env python3
# coding:utf8
#
from flask import Flask, render_template, request, redirect, session
import functools

app=Flask(__name__,template_folder='.',static_url_path='/xxxxxx')
app.secret_key = "sdfasdfasdf3fsdf"
authorized = [('nan', '123', 'Cloud Development Engineer'), ('zhe', '456', 'Product Manager')]

def verify(challenge, authorized):
    for item in authorized:
        if item[0] == challenge[0] and item[1] == challenge[1]:
            return item[2]
    return None
    


def wapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        if not session.get('user_name') and request.path != "/login":
            return redirect('/login')
        return func(*args,**kwargs)
    return inner

@app.route('/')
@app.route('/login',methods=['GET','POST','DELETE'])
@wapper
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        # if user =='zxc' and pwd == '123':
        challenge = (user, pwd)
        info = verify(challenge, authorized)
        if info != None:
            session['user_name'] = user
            session['user_info'] = info
            # print(session['user_name'])
            return redirect('/index')
        else:
            return render_template('login.html',msg='Failed!')
    # logout
    else:
        pass
            

@app.route('/index',methods=['GET'])
@wapper
def index():
    user = session['user_name']
    info = session['user_info']
    return  render_template('/index.html', user=user, info=info)
    

@app.route('/logout', methods=['GET'])
@wapper
def logout():
    session.pop('user_name')
    # return  render_template('/login.html')
    return redirect('/index')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
