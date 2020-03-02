from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

mydb = SQLAlchemy()
migrate = Migrate()
# flask-session-1
# session = Session()

def init_ext(app):
    mydb.init_app(app)
    migrate.init_app(app,mydb)
    # flask-session-2
    # session.init_app(app)