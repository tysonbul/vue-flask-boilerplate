from flask import Blueprint, jsonify, request, redirect
import traceback
import os

from .exceptions import CustomException

errors = Blueprint('errors', __name__)


def register_handlers(app):
    app.register_error_handler(404, __not_found)
    app.register_blueprint(errors)


def __not_found(e):
    if 'api/v' in request.path:
        return __route_not_found(e)
    else:
        return __page_not_found(e)


def __route_not_found(e):
    return 'Route Not Found', 404


def __page_not_found(e):
    return redirect('/#/404')


@errors.app_errorhandler(CustomException)
def handle_error(error):
    print(traceback.format_exc())
    message = [str(x) for x in error.args]
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }
    if os.getenv('NODE_ENV') != 'production':
        response['stacktrace'] = traceback.format_exc()

    return jsonify(response), status_code


@errors.app_errorhandler(Exception)
def __handle_unexpected_error(error):
    print(traceback.format_exc())
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }
    if not os.getenv('NODE_ENV') or os.getenv('NODE_ENV') == 'development':
        response['stacktrace'] = traceback.format_exc()

    return jsonify(response), status_code
