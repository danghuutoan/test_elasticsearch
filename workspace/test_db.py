from sqlalchemy import create_engine, text, Table, Column, Integer, String, Numeric, DateTime, ARRAY, ForeignKey, BigInteger, MetaData
from sqlalchemy.orm import sessionmaker, relationship
import string
import uuid
import random
from sqlalchemy.ext.declarative import declarative_base
from mimesis import Person, Datetime as FakeDateTime, Text
person = Person()
datetime = FakeDateTime()
fake_text = Text()
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
   release_year = Column(Integer)
   language_id = Column(Integer)
   rental_duration = Column(Integer)
   rental_rate = Column(Numeric(4,2))
   length = Column(Integer)
   replacement_cost = Column(Numeric(5,2))
   last_update = Column(DateTime)
   special_features = Column(ARRAY(String))
   actors = relationship("Actor",
                    secondary='film_actor', back_populates="films")

class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    last_update = Column(DateTime)
    films = relationship("Film",
                    secondary='film_actor', back_populates="actors")





meta.create_all(engine)

with engine.connect() as conn:
    Session = sessionmaker(bind = engine)
    with Session() as session:
  
        # row_num = session.query(Actor).count()
        # while row_num < 200:
        #     actor = Actor(first_name=person.first_name(), last_name=person.last_name(), last_update=datetime.datetime())
        #     session.add(actor)
        #     session.commit()
        #     row_num = session.query(Actor).count()
        row_num = session.query(Film).count()
        while row_num < 1000000:
            film = Film(
            title= fake_text.title(), 
            description= fake_text.quote(), 
            release_year= random.randint(2007,2021),
            language_id= random.randint(1, 6),
            rental_duration = random.randint(1, 30),
            rental_rate =  random.randint(1,4),
            length = random.randint(1,200),
            replacement_cost = random.randint(1,100),
            last_update = datetime.datetime(),
            special_features = [fake_text.words()]
            )
            actor = session.query(Actor).get(random.randint(1,200))
            film.actors.append(actor)
            
            
            session.add(film)
            session.commit()
            row_num = session.query(Film).count()

    # for i in range(1,100):
    #     with Session() as session:
    #         x = session.query(Film).get(i)
    #         print(x.__dict__)
    #         x.title = uuid.uuid4().hex
    #         session.commit()

        

# print(string.ascii_uppercase)
# film = Film(
#     title= string.ascii_lowercase, 
#     description= string.ascii_lowercase, 
#     release_year= random.randint(2007,2021),
#     language_id= random.randint(1, 6),
#     rental_duration = random.randint(1, 30),
#     rental_rate =  random.randint(1,4),
#     length = random.

#     )
# session.add(film)
# session.commit()
# row_num = session.query(Film).count()
# print(row_num)
# film = Films()
# for r in result:
#     print(r.__dict__)