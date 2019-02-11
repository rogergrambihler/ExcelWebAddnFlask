"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, make_response, request
from website import app

# Blueprints
from website.manifests import manifests
app.register_blueprint(manifests.routes)

from website.showtaskpane import showtaskpane
app.register_blueprint(showtaskpane.routes)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
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

  #  foo = ""
  #  for attr in dir(request):
   #     foo += str(attr) + ":" + str(getattr(request, attr))

    return render_template(
        'about.html',
        title='About ', # + request.host_url + " " + foo ,
        year=datetime.now().year,
        message='Your application description page.'
    )
