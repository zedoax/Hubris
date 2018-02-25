from flask import Blueprint

squeue_blueprint = Blueprint('squeue_blueprint', __name__, template_folder='templates')

from squeue import routes
