"""
Files: db_add.py
    Insert items into database tables
    @date_modified - 03/08/2018
    @author - Elijah Bendinsky
"""
from sqlalchemy import exc
from database import ENGINE, LOGGER


def create_tournament(data):
    """
    Methods: create_tournament
    Args:
        data: error checked form data to be added as a tournament
    Returns:
        bool -- True on success, False on failure (Default: False)
    """
    try:
        conn = ENGINE.connect()
        conn.execute(
            "INSERT INTO tournament ("
            "tournament_id, title, date, game_title, tourney_type, rule_set) VALUES ('" +
            data['tournament_id'] + "', '" + data['title'] + "', '" + data['date'] + "', '" +
            data['game_title'] + "', '" + data['tourney_type'] + "', '" + data['rule_set'] + "');")
    except exc.DisconnectionError:
        LOGGER.error("Error connecting to database")
        return False
    return True
