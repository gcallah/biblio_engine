#!/bin/bash
# Deploys a new version to our server (run by GitHub Actions on every push
# to master): pulls the code there, migrates the live database and
# reloads the site.
#
# The live database (~/mysite/db.sqlite3 on PythonAnywhere) is the master
# copy: editors change it through the site, and it is no longer in git.
# Every deploy first backs it up to ~/db_backups (keeping the last 30).
# When the server's checkout still tracks db.sqlite3 (the deploy that
# stops tracking it), the live copy is put back after the pull, so the
# pull can neither fail on it nor delete it.
#
# Usage: ./deploy.sh <PA password> <PA API token>
#
# Which site and server: these environment variables, which default to
# the Oakeshott site.
#   PA_USER                 PythonAnywhere account (moabiblio)
#   PA_VENV                 virtualenv in ~/.virtualenvs (biblio)
#   PA_WSGI                 WSGI file to touch for a reload
#                           (/var/www/<account>_pythonanywhere_com_wsgi.py)
#   DJANGO_SETTINGS_MODULE  the site's settings (mysite.settings)
# The checkout is ~/mysite on every server. After the migrations,
# collectstatic gathers the static files into ~/mysite/static_collected,
# which the Web tab's /static/ mapping serves.

PA_USER=${PA_USER:-moabiblio}
PA_VENV=${PA_VENV:-biblio}
PA_WSGI=${PA_WSGI:-/var/www/${PA_USER}_pythonanywhere_com_wsgi.py}
DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-mysite.settings}

echo "SSHing to PythonAnywhere as $PA_USER ($DJANGO_SETTINGS_MODULE)."
# the remote script is quoted, so its settings go in through the
# environment
sshpass -p "$1" ssh -o "StrictHostKeyChecking no" \
    $PA_USER@ssh.pythonanywhere.com \
    "PA_API='$2' PA_USER='$PA_USER' PA_VENV='$PA_VENV' PA_WSGI='$PA_WSGI' \
     DJANGO_SETTINGS_MODULE='$DJANGO_SETTINGS_MODULE' bash -s" << 'EOF'
set -u
export PA_USER PA_VENV PA_WSGI DJANGO_SETTINGS_MODULE
cd ~/mysite
mkdir -p ~/db_backups
stamp=$(date +%Y%m%d-%H%M%S)
backup=~/db_backups/db-$stamp.sqlite3
# sqlite3's .backup copies consistently even if the site writes meanwhile
if command -v sqlite3 > /dev/null; then
    sqlite3 db.sqlite3 ".backup '$backup'"
else
    cp -p db.sqlite3 "$backup"
fi || { echo "Could not back up db.sqlite3"; exit 1; }
echo "Backed up the live database to $backup"
ls -1t ~/db_backups/db-*.sqlite3 | tail -n +31 | xargs -r rm --

tracked=no
if git ls-files --error-unmatch db.sqlite3 > /dev/null 2>&1; then
    tracked=yes
    git checkout -- db.sqlite3   # a clean tree, so the pull can proceed
fi

./rebuild.sh "$PA_API"
status=$?

if [ "$tracked" = yes ] || [ ! -f db.sqlite3 ]; then
    cp -p "$backup" db.sqlite3
    echo "Restored the live database from $backup"
fi
[ "$status" -eq 0 ] || exit "$status"

# from here on, any failure (e.g. a migration) fails the deploy
set -e
set +u   # virtualenv's activate script may read unset variables
source ~/.virtualenvs/$PA_VENV/bin/activate
python manage.py migrate --noinput
# no --clear: files left from an earlier version keep serving pages that
# still ask for them until the reload below
python manage.py collectstatic --noinput -v0
touch "$PA_WSGI"
EOF
