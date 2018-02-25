from flask import Blueprint

tournament_blueprint = Blueprint('tournament_blueprint', __name__, template_folder='templates')

from tournament import routes
