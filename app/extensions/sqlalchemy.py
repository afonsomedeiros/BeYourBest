from flask_sqlalchemy import SQLAlchemy

from settings import ROOT_PATH

orm = SQLAlchemy()

def install(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{ROOT_PATH}/database.sqlite3"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    orm.init_app(app)
    app.db = orm
