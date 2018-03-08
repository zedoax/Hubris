"""
Files: routes.py
    Provides api calls for backend services and database interaction
    @date_modified - 03/08/18
    @author - Elijah Bendinsky
"""
import random
import string
from flask import Blueprint, session, request, jsonify, redirect, url_for
from squeue.queue import SQueue
from database import db_add

BLUEPRINT = Blueprint('api', __name__, template_folder='templates')


@BLUEPRINT.route('/add', methods=['POST'])
def add_player():
    """
    Methods: add_player
        Adds a player from form data given to the queue
    Returns:
        json, int -- result, status code
    """
    if 'players' not in session.keys():
        return jsonify(error='No queue object found'), 404
    players = session.get('players')
    queue = SQueue()
    queue.reconstitute(players)
    if 'new-player' in request.form:
        player = request.form['new-player']
        queue.enqueue(player)
    else:
        return jsonify(error='No/Wrong request arguments found')
    session['players'] = queue.players
    return jsonify(message='Added player'), 201


@BLUEPRINT.route('/move', methods=['POST'])
def move_player():
    """
    Methods: move_player
        Send player to the bottom of the queue
    Returns:
        json, int -- result, status code
    """
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


@BLUEPRINT.route('/remove', methods=['POST'])
def remove_player():
    """
    Methods: remove_player
        Drop player from the queue
    Returns:
        json, int -- result, status code
    """
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


@BLUEPRINT.route('/create', methods=['POST'])
def create():
    """
    Methods: create
        Verifies form data, and adds tournament to the database
    Returns:
        json, int -- response, status code (Default: 500/400 error)
    """
    # TODO: Check for SSO Token
    if {"titleForm", "datepicker", "gameselect", "tourneyselect", "competitors", "admins", "rules"}\
            .issubset(request.form):
        return jsonify(message="Error, mismatched form"), 400
    create_request_data = {
        'tournament_id':
            ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(25)),
        'title': request.form['titleForm'],
        'date': request.form['datepicker'],
        'game_title': request.form['gameselect'],
        'tourney_type': request.form['tourneyselect'],
        'competitors': request.form['competitors'],
        'admins': request.form['admins'],
        'rule_set': request.form['rules']
    }
    if db_add.create_tournament(create_request_data):
        return redirect(url_for('tournament_blueprint.get_tourney'), 302)
    return jsonify(message="Error, tournament not created"), 500
