from flask import Flask

def createApp():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'codey123'

    from .helpers import add_routes
    add_routes(app)

    return app
