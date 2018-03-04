from database import engine
from sqlalchemy import exc
import logging
import os

def init_database(script):
    if engine.has_table("tournament") and engine.has_table("rules") and \
            engine.has_table("match") and engine.has_table("team"):
        logging.info("Database exists, and is proper")
        return True
    try:
        conn = engine.connect()
    except exc.DisconnectionError:
        logging.error("Could not connect to database")
        return False
    transaction = conn.begin()
    try:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, script), 'r') as init_script_file:
            line = init_script_file.readline()
            result = engine.execute(line)
        init_script_file.close()
        transaction.commit()
        logging.info("Database has been setup")
    except IOError:
        logging.error("Creation script not found")
        return False
    except:
        transaction.rollback()
        logging.error("Generic database error")
        return False
    return True
