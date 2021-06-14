from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime, ARRAY, ForeignKey, BigInteger, MetaData
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:ninja-password@db/film_test')
meta = MetaData()
Base = declarative_base(metadata=meta)

class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(Integer, ForeignKey('actor.actor_id'), primary_key=True)
    film_id = Column(BigInteger, ForeignKey('film.film_id'), primary_key=True)
    last_update = Column(DateTime)

class Film(Base):
   __tablename__ = 'film'
   film_id = Column(BigInteger, primary_key=True, autoincrement=True)
   title = Column(String)
   description = Column(String)
#    release_year = Column(Integer)
#    language_id = Column(Integer)
#    rental_duration = Column(Integer)
#    rental_rate = Column(Numeric(4,2))
#    length = Column(Integer)
#    replacement_cost = Column(Numeric(5,2))
#    last_update = Column(DateTime)
#    special_features = Column(ARRAY(String))
   actors = relationship("Actor",
                    secondary='film_actor', back_populates="films")

class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    # last_update = Column(DateTime)
    films = relationship("Film",
                    secondary='film_actor', back_populates="actors")