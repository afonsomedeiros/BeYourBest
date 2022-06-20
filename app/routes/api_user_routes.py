from flask import Flask

from app.api import user

def create_routes(app: Flask):
    app.add_url_rule("/user/new", methods=["POST"], view_func=user.signup_user)
    app.add_url_rule("/professional/new", methods=["POST"], view_func=user.signup_professional)