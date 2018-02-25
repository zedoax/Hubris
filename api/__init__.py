from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')

from api import routes
