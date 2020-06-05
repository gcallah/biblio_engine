#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

export user_name=gcallah
export project_name=mysite
export virtual_env=biblio
export WSGI_configuration_file=/var/www/gcallah_pythonanywhere_com_wsgi.py

# get new source code onto the server
git pull origin master
# activate our virtual env:
source /home/$user_name/.virtualenvs/$virtual_env/bin/activate
# install all of our packages:
pip install -r requirements/requirements.txt
echo "Going to reboot the webserver"
touch WSGI_configuration_file
