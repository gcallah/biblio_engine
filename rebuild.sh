#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

export user_name=wm1065
export project_name=mysite
export WSGI_configuration_file=/var/www/wm1065_pythonanywhere_com_wsgi.py

# get new source code onto the server
git pull origin master
# activate our virtual env:
source /home/$user_name/.virtualenvs/$project_name/bin/activate
# install all of our packages:
pip install -r requirements/requirements.txt
echo "Going to reboot the webserver"
touch WSGI_configuration_file
