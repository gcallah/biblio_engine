#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

# deploy.sh passes in which site (the defaults are the Oakeshott site's)
user_name=${PA_USER:-moabiblio}
virtual_env=${PA_VENV:-biblio}
WSGI_configuration_file=${PA_WSGI:-/var/www/${user_name}_pythonanywhere_com_wsgi.py}

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
