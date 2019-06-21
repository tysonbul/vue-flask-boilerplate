from flask import Blueprint, g
from .v0 import get_routes as get_v0_routes
from .content import main


def register_routes(app):
    """Register routes with the blueprint API

    Arguments:
        app {FlaskApp} -- The flask app
    """
    app.register_blueprint(main, url_prefix='')
    app.register_blueprint(get_v0_routes(), url_prefix='/api/v0')
    # app.register_blueprint(get_v1_routes(), url_prefix='/api/v1') # for when we add new version of routes, this is how itll be done.
