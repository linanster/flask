#! /usr/bin/env python3
# coding:utf8
#
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='.')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=True)
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(10))
    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def index():
    return render_template('index.html', students = Students.query.all() )

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        city = request.form.get('city')
        addr = request.form.get('addr')
        pin = request.form.get('pin')
        if not name or not city or not addr:
            flash('Please enter all the required fields', 'error')
            return render_template('add.html', id=id, name=name, city=city, addr=addr, pin=pin)
        else:
            # 添加
            if id == '':
                student = Students(name, city, addr, pin)
                db.session.add(student)
                flash('Record was successfully added')            
            # 编辑            
            else:
                student = Students.query.get(id)
                student.name = name
                student.city = city
                student.addr = addr
                student.pin = pin
                flash('Record was successfully updated')            
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add.html')
    
@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        id = request.form.get('id')
    else:
        id = request.args.get('id')
    # 删除
    student = Students.query.get(id)
    db.session.delete(student)
    db.session.commit()
    flash('Record was successfully deleted')
    return redirect(url_for('index'))

@app.route('/edit', methods=['GET','POST'])
def edit():
    if request.method == 'POST':
        id = request.form.get('id')
    else:
        id = request.args.get('id')
    student = Students.query.get(id)
    # return render_template('add.html', student=student)
    return render_template('add.html', id=student.id, name=student.name, city=student.city, addr=student.addr, pin=student.pin)



if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)