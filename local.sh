#!/bin/sh
# Run the app locally at http://127.0.0.1:8000/oakeshott/

cd "$(dirname "$0")"

# Use the project's virtualenv if there is one.
PY=python3
[ -x .venv/bin/python ] && PY=.venv/bin/python

echo "Spinning up webserver: open http://127.0.0.1:8000/oakeshott/"
exec $PY ./manage.py runserver 127.0.0.1:8000
