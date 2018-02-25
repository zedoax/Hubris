from tournament import tournament_blueprint
from flask import render_template


@tournament_blueprint.route("/tournament", methods=['GET', 'POST'])
def get_tourney():
    return render_template('tournament.html', title='CSH | Tournament')


@tournament_blueprint.route("/create", methods=['GET'])
def get_create():
    return render_template('create.html', title='CSH | Tournament')

