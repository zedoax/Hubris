from database import db, engine


class Tournament(db.Model):
    __tablename__ = 'tournament'
