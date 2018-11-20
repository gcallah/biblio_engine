#!/bin/sh

echo "Spinning up webserver."
python3 ./manage.py runserver 0.0.0.0:8000
