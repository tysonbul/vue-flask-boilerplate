from . import routes
from ..exceptions import CustomException


@routes.route('/test')
def test_success():
    return "Success!"


@routes.route('/test/error')
def test_error():
    0/0
    return "Shouldn't get here!"


@routes.route('/test/error/custom')
def test_error_custom():
    try:
        0/0
    except ZeroDivisionError as e:
        raise CustomException("Try to divide by zero")
    return "Shouldn't get here!"
