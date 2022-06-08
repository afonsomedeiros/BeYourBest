from flask import Flask

from app.controllers import home

def create_routes(app: Flask):
    app.add_url_rule("/", methods=["GET"], view_func=home.index)