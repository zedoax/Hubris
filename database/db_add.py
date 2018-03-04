from sqlalchemy import exc
from database import engine
import logging


def create_tournament(data):
    try:
        conn = engine.connect()
        conn.execute(
            "INSERT INTO tournament ("
            "tournament_id, title, date, game_title, tourney_type, rule_set) VALUES ('" +
            data['tournament_id'] + "', '" + data['title'] + "', '" + data['date'] + "', '" +
            data['game_title'] + "', '" + data['tourney_type'] + "', '" + data['rule_set'] + "');")
    except exc.DisconnectionError:
        logging.error("Error connecting to database")
        return False
    return True
