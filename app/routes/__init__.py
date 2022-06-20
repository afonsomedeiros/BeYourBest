from . import api_user_routes


def create_all_routes(app):
    api_user_routes.create_routes(app)