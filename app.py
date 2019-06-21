import os

from server import create_app

app = create_app(os.getenv('NODE_ENV') or 'default')

if __name__ == "__main__":
    debug = app.config.get('DEBUG', True)
    app.run(port=5000, host='0.0.0.0', threaded=True, debug=debug)
