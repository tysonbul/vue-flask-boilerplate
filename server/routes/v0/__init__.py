from flask import Blueprint, g
routes = Blueprint('api_v0', __name__)


def get_routes():
    from . import test
    return routes
