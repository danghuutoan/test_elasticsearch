import socket
from models import Film, engine
from sqlalchemy.orm import sessionmaker
import json
import time
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch(["http://elasticsearch:9200"], maxsize=25)

host = "127.0.0.1"
port = 5000


def post_process(film):
    actors = []
    result = film.__dict__

    for actor in film.actors:
        tmp = actor.__dict__
        tmp.pop('_sa_instance_state')
        actors.append(tmp)

    result.pop('_sa_instance_state')
    result["actors"] = actors
    return result


start = time.time()

offset = 0
with engine.connect() as conn:
    Session = sessionmaker(bind=engine)
    with Session() as session:
        films = session.query(Film).order_by(Film.film_id).all()
        actions = [
            {
                "_index": "films",
                "_type": "_doc",
                "_id": film.film_id,
                "_source": dict(post_process(film))
            }
            for film in films
        ]

        helpers.bulk(es, actions)

print(f"finishes in {time.time() - start}")
