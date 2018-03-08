""" Top level module for running Hubris"""
import logging
from flask import Flask
import config
from squeue.routes import BLUEPRINT as SQUEUE_BLUEPRINT
from api.routes import BLUEPRINT as API_BLUEPRINT
from database import db_init
from tournament import BLU

LOGGER = logging.getLogger(__name__)

# Declare the application
APP = Flask(__name__, static_url_path='/static')

# Load configuration
APP.secret_key = config.SECRET_KEY
APP.config.from_pyfile('config.py')

# Register blueprints
APP.register_blueprint(API_BLUEPRINT, url_prefix='/api/v1')
APP.register_blueprint(SQUEUE_BLUEPRINT, url_prfix='/')
APP.register_blueprint(tournament_blueprint, url_prefix='/tournament')

db_init.database_check_init()

if __name__ == '__main__':
    APP.run()
