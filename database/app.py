from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='.')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class students(db.Model):
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
    return render_template('index.html', students = students.query.all() )

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            # 编辑
            if request.form.get('id'):
                id = request.form['id']
                student = students.query.get(id)
                student.name = request.form['name']
                student.city = request.form['city']
                student.addr = request.form['addr']
                student.pin = request.form['pin']
                # db.session.commit()
                flash('Record was successfully updated')            
            # 添加
            else:
                student = students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
                db.session.add(student)
                # db.session.commit()
                flash('Record was successfully added')
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add.html')
    
@app.route('/delete')
def delete():
    id = request.args.get('id')
    
    # 删除
    student = students.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit')
def edit():
    id = request.args.get('id')
    student = students.query.get(id)
    return render_template('add.html', student=student)


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')