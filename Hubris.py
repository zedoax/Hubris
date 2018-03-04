from flask import Flask
import config
from api import api_blueprint
from squeue import squeue_blueprint
from tournament import tournament_blueprint
from database import db_init

app = Flask(__name__, static_url_path='/static')
app.secret_key = config.SECRET_KEY
app.config.from_pyfile('config.py')
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
app.register_blueprint(squeue_blueprint)
app.register_blueprint(tournament_blueprint, url_prefix='/tournament')


if __name__ == '__main__':
    app.run()
