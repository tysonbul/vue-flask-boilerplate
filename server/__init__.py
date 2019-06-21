from flask import Flask
from config import config

from .routes import register_routes
from .routes.handlers import register_handlers


def create_app(config_name):
    """Creates the app instance

    Arguments:
        config_name {string} -- name of the config envrionment to use (staging, development,...)

    Returns:
        FlaskApp -- flask app object
    """

    app = Flask(__name__, template_folder="../dist",
                static_folder="../dist", static_url_path='')
    app.config.from_object(config[config_name])

    with app.app_context():
        register_routes(app)
        register_handlers(app)

    return app
