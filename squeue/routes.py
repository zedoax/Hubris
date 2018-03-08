"""
Files: routes.py
    @date_modified - 03/08/18
    @author - Elijah Bendinsky
"""
from flask import Blueprint, render_template, session
from . import queue

BLUEPRINT = Blueprint('squeue_blueprint', __name__, template_folder='templates')


@BLUEPRINT.route('/', methods=['GET'])
def get_squeue():
    """
    Methods: get_squeue
        Renders a page with the current queue population
        # If there is no queue, make one
    Returns:
        text -- The rendered web page w/queue (default: rendered webpage w/out queue)
    """
    if 'players' not in session.keys():
        # Initialize a new queue if the current session has none
        session['players'] = queue.SQueue().players
    players = session.get('players')
    return render_template('squeue.html', title='CSH | Smash Queue', players=players)
