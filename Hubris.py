from flask import Flask
from api import api_blueprint
from squeue import squeue_blueprint
from tournament import tournament_blueprint
from config import SECRET_KEY
from database import db as model_db

app = Flask(__name__, static_url_path='/static')
app.secret_key = SECRET_KEY
app.config.from_pyfile('config.py')
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
app.register_blueprint(squeue_blueprint)
app.register_blueprint(tournament_blueprint, url_prefix='/tournament')

model_db.init_app(app)
with app.app_context():
    model_db.init_app()


if __name__ == '__main__':
    app.run()
