#! /usr/bin/env python3
# coding:utf8
#
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__, template_folder='.')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@10.30.30.101:3306/getest'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app, use_native_unicode='utf8')

class tb_courses(db.Model):
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key = True)
    code = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    def __init__(self, code, name, credit, description=None):
        self.code = code
        self.name = name
        self.credit = credit
        self.description = description

class tb_students(db.Model):
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    course_code = db.Column(db.Integer, db.ForeignKey('tb_courses.code'), nullable=False)
    age = db.Column(db.Integer)
    def __init__(self, name, course_code, age):
        self.name = name
        self.course_code = course_code
        self.age = age



if __name__ == '__main__':
    # print('create tables:')
    # db.create_all()
    # db.drop_all()
    stu1 = tb_students('Zhe', 1, 29)
    stu2 = tb_students('Bob', 2, 37)
    db.session.add(stu1)
    db.session.add(stu2)
    db.session.commit()