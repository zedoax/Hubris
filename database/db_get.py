from sqlalchemy import exc
from database import engine
import logging
import json


def get_tournaments():
    try:
        conn = engine.connect()
    except exc.DisconnectionError:
        logging.error("Error connecting to database")
        return None
    result = conn.execute("SELECT * FROM tournament")
    tournament = []
    for row in result:
        tournament.append(json.dumps(row))
    conn.close()
    return json.dumps(tournament)



