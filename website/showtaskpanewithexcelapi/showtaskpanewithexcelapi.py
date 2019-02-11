
from flask import Blueprint, request, render_template, make_response

routes = Blueprint('manifests', __name__, url_prefix='/manifests', template_folder='templates',  static_folder='static')

@routes.route('/manifest.xml', methods=['GET'])
def manifestXml():

    # Office Agaves requires the urls to be https so 
    # replace the host_url information in the manifest
    # to be the current request's HTTP_HOST with the https 
    # protocol. 
    # todo: possible browsed to this page as http:// instead of https://
    # in which case if using non-standard ports this can be wrong. 

    host_url = "https://" + request.host + "/"
    responseXml = render_template(
        'manifest.xml',
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
