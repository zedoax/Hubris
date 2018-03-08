from flask import Blueprint, render_template

BLUEPRINT = Blueprint('tournament_blueprint', __name__, template_folder='templates')


@BLUEPRINT.route("/", methods=['GET', 'POST'])
def get_tourney():
    return render_template('tournament.html', title='CSH | Tournament', enabled=False)


@BLUEPRINT.route("/create", methods=['GET'])
def get_create():
    return render_template('create.html', title='CSH | Tournament')


@BLUEPRINT.route("/<tournament_id>", methods=['GET', 'POST'])
def get_view_tournament(tournament_id):
    return render_template('view_tournament.html', title='CSH | Tournament')


@BLUEPRINT.route("/<tournament_id>/rules", methods=['GET', 'POST'])
def get_view_rules(tournament_id):
    return render_template('view_rules.html', title='CSH | Tournament')