from .blue1 import blue1
from .blue2 import blue2
from .blue3 import blue3


def init_views(app):
    app.register_blueprint(blue1)
    app.register_blueprint(blue2)
    app.register_blueprint(blue3)
