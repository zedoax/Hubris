from database import engine
import logging


def database_check_init():
    if engine.has_table("tournament") and engine.has_table("rules") and \
            engine.has_table("match") and engine.has_table("team"):
        logging.info("Database exists, and is proper")
        return True
    logging.error("Database does not exist or is not proper")
    return False
