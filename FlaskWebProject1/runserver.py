"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app


if __name__ == '__main__':

    # If launched as main then setup the Flask Server
    HOST = environ.get('SERVER_HOST', 'localhost')
    PORT = int(environ.get('SERVER_PORT', '50603'))

    # https://localhost:50603
    app.run(HOST, PORT, debug=True, ssl_context=('certs/server.crt', 'certs/server.key'))
