#!/bin/sh
docker rm biblio 2> /dev/null || true 
docker run -it -e "USE_MYSQL=0" -p 8000:8000 -v $PWD:/home/biblio_engine biblio bash
