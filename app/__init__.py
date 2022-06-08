from flask import Flask

from .routes import home_route

def create_app():
    app = Flask(__name__)

    home_route.create_routes(app)

    return app