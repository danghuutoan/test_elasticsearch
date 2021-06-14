import socket
from models import Film, engine
from sqlalchemy.orm import sessionmaker
import json
import time

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
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            for film in films:
                # print(film.film_id)
                result = post_process(film)
                sock.send(json.dumps(dict(result)).encode('utf-8'))

print(f"finishes in {time.time() - start}")
