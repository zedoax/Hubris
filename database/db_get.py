"""
Files: db_get.py
    Query database for information
    @date_modified - 03/08/18
    @author - Elijah Bendinsky
"""
import logging
import json
from sqlalchemy import exc
from database import ENGINE


def get_tournaments():
    """
    Methods: get_tournaments
        Get list of ongoing tournaments and their metadata
    Returns:
        string -- Json formatted list of Json objects containing
          tournament items (default: empty string)
    """
    try:
        conn = ENGINE.connect()
    except exc.DisconnectionError:
        logging.error("Error connecting to database")
        return ""
    result = conn.execute("SELECT * FROM tournament")
    tournament = []
    for row in result:
        tournament.append(json.dumps(row))
    conn.close()
    return json.dumps(tournament)
