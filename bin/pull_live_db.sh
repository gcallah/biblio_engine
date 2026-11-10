#!/bin/bash
# Download the live database (the master copy, on PythonAnywhere) over the
# local db.sqlite3, after backing the local one up. Do this before any bulk
# load, then check the result and upload it with bin/push_live_db.sh.
#
# Needs the moabiblio account's password in MOABIBLIO_PWD.
# Usage: bin/pull_live_db.sh
set -euo pipefail
cd "$(dirname "$0")/.."
: "${MOABIBLIO_PWD:?Set MOABIBLIO_PWD to the moabiblio PythonAnywhere password}"
REMOTE=moabiblio@ssh.pythonanywhere.com
[ -f db.sqlite3 ] && bin/backup_db.sh before-pull
sshpass -p "$MOABIBLIO_PWD" scp -o StrictHostKeyChecking=no \
    "$REMOTE:mysite/db.sqlite3" db.sqlite3.download
mv db.sqlite3.download db.sqlite3
# remember which live copy this is, so push_live_db.sh can tell whether
# anyone has edited the site since
shasum db.sqlite3 | cut -d' ' -f1 > db.sqlite3.live-sha
echo "Downloaded the live database to db.sqlite3."
