from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc, MetaData
import config
import logging

try:
    db = SQLAlchemy()
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    metadata = MetaData()
    metadata.reflect(engine)
except exc.DBAPIError:
    logging.error("Unable to connect to database")
except exc.SQLAlchemyError:
    logging.error("SQLAlchemy gone wild")
