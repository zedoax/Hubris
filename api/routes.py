from api import api_blueprint


@api_blueprint.route('/createQueue', methods=['POST'])
def create_queue():
    return 'createqueue'


@api_blueprint.route('/add', methods=['POST'])
def add_player():
    return 'addplayer'


@api_blueprint.route('/move', methods=['POST'])
def move_player():
    return 'moveplayer'


@api_blueprint.route('/remove', methods=['POST'])
def remove_player():
    return 'removeplayer'