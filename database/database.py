from database import engine, conn
import logging


def init_database(script):
    if engine.has_table("tournament") and engine.has_table("rules") and engine.has_table("match") and engine.has_table("team"):
        logging.info("Database exists, and is proper")
        return True
    transaction = conn.begin()
    try:
        init_script = open(script, 'r')
        for line in init_script.read():
            transaction.execute(line)
        init_script.close()
        transaction.commit()
        logging.info("Database has been setup")
    except IOError:
        logging.error("Creation script not found")
        raise
    except:
        transaction.rollback()
        logging.error("Generic database error")
        raise
    return True
