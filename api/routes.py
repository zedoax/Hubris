from api import api_blueprint
from flask import session, request, jsonify
from squeue.queue import SQueue


@api_blueprint.route('/add', methods=['POST'])
def add_player():
    r = request
    if 'players' not in session.keys():
        return jsonify(error='No queue object found'), 404
    players = session.get('players')
    queue = SQueue()
    queue.reconstitute(players)
    player = request.json['player']
    queue.enqueue(player)
    session['players'] = queue.players
    return jsonify(message='Added player'), 201


@api_blueprint.route('/move', methods=['POST'])
def move_player():
    if 'players' not in session.keys():
        return jsonify(error='No queue object found'), 404
    players = session.get('players')
    queue = SQueue()
    queue.reconstitute(players)
    player = queue.dequeue()
    queue.enqueue(player)
    session['players'] = queue.players
    return jsonify(message='Player moved'), 200


@api_blueprint.route('/remove', methods=['POST'])
def remove_player():
    if 'players' not in session.keys():
        return jsonify(error='No queue object found'), 404
    players = session.get('players')
    index = request['index']
    queue = SQueue()
    queue.reconstitute(players)
    queue.remove(index)
    session['players'] = queue.players
    return jsonify(message='Player removed'), 200


@api_blueprint.route('/create', methods=['POST'])
def create():
    """
    r = request
    title = r.form['titleForm']
    date = r.form['datepicker']
    game = r.form['gameselect'] #deal with inputting own game
    type = r.form['tourneyselect']
    competitors = r.form['competitors'] #deal with member-complete; deal with counting competitors
    admins = r.form['admins'] #deal with member-complete
    rules = r.form['rules'] #deal with porting; text file maybe?
    """
