#!/usr/bin/python3
""" This module prepare flask blueprint
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv
from flask_cors import CORS
from flasgger import Swagger


app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def shutdown_session(exception=None):
    """ This method close the session
    """
    storage.close()


@app.errorhandler(404)
def error404(error):
    """ error 404 handler """
    return jsonify({
            'error': 'Not found'
        }), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = 5000
    app.run(host=host, port=port, threaded=True)
