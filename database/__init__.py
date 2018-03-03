from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc
import config, logging

try:
    db = SQLAlchemy()
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    conn = engine.connect()
except exc.DBAPIError:
    logging.error("Unable to connect to database")
except exc.SQLAlchemyError:
    logging.error("SQLAlchemy gone wild")
