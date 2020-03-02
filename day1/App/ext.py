from flask_sqlalchemy import SQLAlchemy

mydb = SQLAlchemy()

def init_ext(app):
    mydb.init_app(app)