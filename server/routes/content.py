from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/heartbeat')
def heartbeat():
    return 'OKAY', 200


@main.route('/index.html')
@main.route('/home')
def index():
    """All routes here should render the index page"""
    return redirect(url_for('main.render_content'))


@main.route('/')
def render_content():
    return render_template("index.html")
