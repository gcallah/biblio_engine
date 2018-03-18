#!/bin/sh
if [ -z "$1" ]
    then
        echo "You must provide the location of your biblio repo."
        exit 1
fi 
docker run -it -p 8000:8000 -v $1:/home/biblio --name biblio gcallah/django:latest bash
