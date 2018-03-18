#!/bin/sh

#Run this from inside your container to launch biblio_engine
#Although *inside* the container the web server runs at0.0.0.0:8000,
#from outside it appeats at 127.0.0.1:8000.

./manage.py runserver 0.0.0.0:8000
