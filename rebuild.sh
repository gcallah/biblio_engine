#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

export user_name=moabiblio
export project_name=mysite
export virtual_env=biblio
export WSGI_configuration_file=/var/www/moabiblio_pythonanywhere_com_wsgi.py

# stop at the first failure (e.g. a git pull that cannot fast-forward), so
# the deploy job fails instead of reporting success on stale code
set -e

# get new source code onto the server
git pull origin master
# activate our virtual env:
source /home/$user_name/.virtualenvs/$virtual_env/bin/activate
# install all of our packages:
pip install -r requirements/requirements.txt
echo "Going to reboot the webserver"
touch $WSGI_configuration_file
