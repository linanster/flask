from flask_sqlalchemy import SQLAlchemy

from App.ext import mydb


class User(mydb.Model):
    id = mydb.Column(mydb.Integer, primary_key=True)
    username = mydb.Column(mydb.String(20))
    age = mydb.Column(mydb.Integer)
    def save(self):
        mydb.session.add(self)
        mydb.session.commit()