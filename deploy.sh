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

export user_name=moabiblio

echo "SSHing to PythonAnywhere."
sshpass -p "$1" ssh -o "StrictHostKeyChecking no" \
    $user_name@ssh.pythonanywhere.com "PA_API='$2' bash -s" << 'EOF'
set -u
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
source ~/.virtualenvs/biblio/bin/activate
python manage.py migrate --noinput
touch /var/www/moabiblio_pythonanywhere_com_wsgi.py
EOF
