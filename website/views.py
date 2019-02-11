"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, make_response, request
from website import app

# Blueprints
from website.manifests import manifests

app.register_blueprint(manifests.routes)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


## todo: app route for generating the manifest.xml
# is there better way to do the approutes vs. all one file?
@app.route('/manifest.xml')
def manifestXml():

    # Office Agaves requires the urls to be https so 
    # replace the host_url information in the manifest
    # to be the current request's HTTP_HOST with the https 
    # protocol. 
    # todo: possible browsed to this page as http:// instead of https://
    # in which case if using non-standard ports this can be wrong. 

    host_url = "https://" + request.host + "/"
    responseXml = render_template(
        'manifests/manifest.xml',
        host_url=host_url
    )

    response = make_response(responseXml)
    response.headers["Cache-Control"] = "must-revalidate"
    response.headers["Pragma"] = "must-revalidate"
    response.headers["Content-type"] = "application/xml"

    # Add the Content-Disposition which will tell the browser to download as a file 
    # instead of showing in the browser
    response.headers["Content-Disposition"] =  "attachment; filename='manifest.xml'"
    return response


@app.route('/addin.html')
def addin():
    """Renders the home page."""
    return render_template(
        'addin.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/functions.html')
def functions():
    """Renders the home page."""
    return render_template(
        'functions.html',
        title='functions page',
        year=datetime.now().year,
    )

@app.route('/dialog.html')
def dialog():
    """Renders the home page."""
    return render_template(
        'dialog.html',
        title='functions page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""

    foo = ""
    for attr in dir(request):
        foo += str(attr) + ":" + str(getattr(request, attr))

    return render_template(
        'about.html',
        title='About ' + request.host_url + " " + foo ,
        year=datetime.now().year,
        message='Your application description page.'
    )
