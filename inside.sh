#!/bin/sh

# Run this from inside your container to launch biblio_engine.
# Inside the container the server must listen on 0.0.0.0:8000 so that
# Docker's port mapping can reach it; from your machine, open the URL below.

echo "Spinning up webserver: open http://127.0.0.1:8000/oakeshott/"
./manage.py runserver 0.0.0.0:8000
