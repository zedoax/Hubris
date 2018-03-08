"""
Files: __init__.py
    Module that provides a connection layer for PostGreSQL
    @date_modified - 03/08/2018
    @author - Elijah Bendinsky
"""
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc, MetaData
import config

LOGGER = logging.getLogger(__name__)

try:
    DB = SQLAlchemy()
    ENGINE = create_engine(config.SQLALCHEMY_DATABASE_URI)
    METADATA = MetaData()
    METADATA.reflect(ENGINE)
except exc.DBAPIError:
    LOGGER.error("Unable to connect to database")
except exc.SQLAlchemyError:
    LOGGER.error("SQLAlchemy gone wild")
