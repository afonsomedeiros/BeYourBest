from flask import Flask
from flask_migrate import Migrate

from .routes import home_route
from .extensions import sqlalchemy
from .models import User, Person, Professional

def create_app():
    app = Flask(__name__)

    home_route.create_routes(app)

    sqlalchemy.install(app)

    migrate = Migrate(app, app.db)

    return app