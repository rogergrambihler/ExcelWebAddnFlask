
from flask import Blueprint, request, render_template, make_response

routes = Blueprint('showtaskpane', __name__, url_prefix='/showtaskpane', template_folder='templates', static_folder='static')

@routes.route('/showtaskpane.html', methods=['GET'])
def showtaskpane():

    return render_template(
        'showtaskpane.html',
        title='Home Page',
    )
