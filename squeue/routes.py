from squeue import squeue_blueprint
from flask import render_template, session
from squeue.queue import SQueue


@squeue_blueprint.route('/', methods=['GET'])
def get_squeue():
    if 'players' not in session.keys():
        session['players'] = SQueue().players
    players = session.get('players')
    return render_template('squeue.html', title='CSH | Smash Queue', players=players)
