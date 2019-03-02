"""
This script runs the FlaskWebProject1 application using a development server.
"""

# gunicorn
# gunicorn --worker-class eventlet -w 1 --certfile cert.pem --keyfile key.pem -b 0.0.0.0:5500 app:app
# gunicorn --worker-class eventlet -w 1 module:app
# Using nginx as a WebSocket Reverse Proxy

# NGinx -> Gunicorn -> Flask/Django
# Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP, developed to power Django Channels.
# What you need is CGI support for lighthttpd.

from os import environ
import ssl
from website import app
from flask_socketio import SocketIO, emit

#from livereload import Server, shell

from submodules.livereload.livereload import Server, shell


ssl_ctx = None
#ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#ssl_ctx.load_cert_chain(
#        "C:\\Users\\rogerg.REDMOND\\source\\repos\\ExcelWebAddnFlask\\website\\certs\\server.pem")


# hack socketio location test
socketio = SocketIO(app, ssl_ctx=ssl_ctx)

if __name__ == '__main__':

    # If launched as main then setup the Flask Server
    HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    PORT = int(environ.get('SERVER_PORT', '50603'))

 #   socketio.run(app, port=9090)


  #  server = Server(app.wsgi_app)
  #  certLocation = "website/certs/"
  #  app.debug = True

    # server.watch
  #  server.watch('website/')
  #  server.watch('website/templates/')


    # server.serve(port=PORT, ssl_ctx=ssl_ctx)

     # https://localhost:50603
    # pass in debug=false since debugging with Visual Studio code.
    certLocation = "website/certs/"

#     app.run(HOST, PORT, debug=False, ssl_context=(certLocation + 'server.crt', certLocation + 'server.key'))
    app.run(HOST, PORT, debug=False)


