from tournament import tournament_blueprint
from flask import render_template


@tournament_blueprint.route("/tournament", methods=['GET'])
def get_tourney():
    return render_template('tournament.html', title='CSH | Tournament')

