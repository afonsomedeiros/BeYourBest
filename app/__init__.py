from flask import Flask
from flask_migrate import Migrate

from .routes import create_all_routes
from .extensions import sqlalchemy
from .models import User, Professional

def create_app():
    app = Flask(__name__)

    sqlalchemy.install(app)

    migrate = Migrate(app, app.db)

    create_all_routes(app)

    return app