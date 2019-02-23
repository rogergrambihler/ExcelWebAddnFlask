"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from website import app
#from livereload import Server, shell

from submodules.livereload.livereload import Server, shell



if __name__ == '__main__':

    # If launched as main then setup the Flask Server
    HOST = environ.get('SERVER_HOST', 'localhost')
    PORT = int(environ.get('SERVER_PORT', '50603'))

    server = Server(app.wsgi_app)
    certLocation = "website/certs/"
    app.debug = True

    # server.watch
    server.watch('website/')
    server.watch('website/templates/')
    server.serve(port=PORT)

     # https://localhost:50603
    # pass in debug=false since debugging with Visual Studio code.
    certLocation = "website/certs/"

#    app.run(HOST, PORT, debug=False, ssl_context=(certLocation + 'server.crt', certLocation + 'server.key'))


