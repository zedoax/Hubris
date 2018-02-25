from flask import Flask
from api import api_blueprint
from squeue import squeue_blueprint
from config import SECRET_KEY
from tournament import tournament_blueprint

app = Flask(__name__, static_url_path='/static')
app.secret_key = SECRET_KEY
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
app.register_blueprint(squeue_blueprint)

app.register_blueprint(tournament_blueprint, url_prefix='/tournament')


if __name__ == '__main__':
    app.run()
