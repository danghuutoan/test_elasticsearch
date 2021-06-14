import socket
import json
host = "127.0.0.1"
port = 5000
from sqlalchemy import create_engine, text
import time

engine = create_engine('postgresql://postgres:ninja-password@db/film_test', echo = True)
conn = engine.connect()
start = time.time()
t = text("SELECT film_id, title, description FROM film")
result = conn.execute(t)

for r in result:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.send(json.dumps(dict(r)).encode('utf-8'))
        print(sock.recv(1024))

print(f"finishes in {time.time() - start}")
