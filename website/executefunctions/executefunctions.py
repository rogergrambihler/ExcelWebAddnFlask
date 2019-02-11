
from flask import Blueprint, request, render_template, make_response

routes = Blueprint('executefunctions', __name__, url_prefix='/executefunctions', template_folder='templates', static_folder='static')

@routes.route('/executefunctions.html', methods=['GET'])
def executefunctions():

    return render_template(
        'executefunctions.html',
        title='Home Page',
    )

@routes.route('/dialog.html')
def dialog():
    """Renders the home page."""
    return render_template(
        'dialog.html',
        title='functions page'
    )