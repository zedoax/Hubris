from api import api_blueprint
from flask import session, request, jsonify
from squeue.queue import SQueue


@api_blueprint.route('/add', methods=['POST'])
def add_player():
    if 'players' not in session.keys():
        return jsonify(error='No queue object found'), 404
    players = session.get('players')
    queue = SQueue()
    queue.reconstitute(players)
    player = request.form['player']
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
    if 'index' in request.form and 'player' in request.form:
        index = int(request.form['index']) - 1
        player = queue.dequeue(index)
        queue.enqueue(player)
    else:
        return jsonify(error='No/Wrong request arguments found')
    session['players'] = queue.players
    return jsonify(message=request.form['player'] + ' moved'), 205


@api_blueprint.route('/remove', methods=['POST'])
def remove_player():
    if 'players' not in session.keys():
        return jsonify(error='No queue object found'), 404
    players = session.get('players')
    queue = SQueue()
    queue.reconstitute(players)
    if 'index' in request.form and 'player' in request.form:
        index = int(request.form['index']) - 1
        queue.remove(index)
    else:
        return jsonify(error='No/Wrong request arguments found'), 404
    session['players'] = queue.players
    return jsonify(message=request.form['player'] + ' removed'), 205


@api_blueprint.route('/create', methods=['POST'])
def create():
    """
    title = request.form['titleForm']
    date = request.form['datepicker']
    game = request.form['gameselect'] #deal with inputting own game
    type = request.form['tourneyselect']
    competitors = request.form['competitors'] #deal with member-complete; deal with counting competitors
    admins = request.form['admins'] #deal with member-complete
    rules = request.form['rules'] #deal with porting; text file maybe?
    """
