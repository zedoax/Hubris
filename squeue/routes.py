from squeue import squeue_blueprint
from flask import render_template, session
from squeue.queue import SQueue
import json


@squeue_blueprint.route('/', methods=['GET'])
def get_squeue():
    if 'queue' not in session.keys():
        session['queue'] = json.dumps(SQueue().players)
    players = session.get('queue')
    return render_template('squeue.html', title='CSH | Smash Queue', players=players)
