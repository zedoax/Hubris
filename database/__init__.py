from sqlalchemy import create_engine
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
conn = engine.connect()
