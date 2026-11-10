#!/bin/bash
# Upload the local db.sqlite3 as the live database, after a bulk load done
# on a copy fetched with bin/pull_live_db.sh. Refuses if the live database
# has changed since that download (someone edited the site), since
# uploading would wipe their edits: pull again and redo the load.
# The live copy it replaces is kept in ~/db_backups on the server.
#
# Needs the moabiblio account's password in MOABIBLIO_PWD.
# Usage: bin/push_live_db.sh
set -euo pipefail
cd "$(dirname "$0")/.."
: "${MOABIBLIO_PWD:?Set MOABIBLIO_PWD to the moabiblio PythonAnywhere password}"
REMOTE=moabiblio@ssh.pythonanywhere.com
[ -f db.sqlite3.live-sha ] || {
    echo "No record of a download: run bin/pull_live_db.sh first."; exit 1; }
run() { sshpass -p "$MOABIBLIO_PWD" ssh -o StrictHostKeyChecking=no \
            "$REMOTE" "$@"; }
live=$(run 'sha1sum ~/mysite/db.sqlite3' | cut -d' ' -f1)
if [ "$live" != "$(cat db.sqlite3.live-sha)" ]; then
    echo "The live database has changed since bin/pull_live_db.sh;" \
         "not uploading. Pull again and redo the load."
    exit 1
fi
sshpass -p "$MOABIBLIO_PWD" scp -o StrictHostKeyChecking=no \
    db.sqlite3 "$REMOTE:mysite/db.sqlite3.upload"
run 'set -e; cd ~/mysite; mkdir -p ~/db_backups
     cp -p db.sqlite3 ~/db_backups/db-before-upload-$(date +%Y%m%d-%H%M%S).sqlite3
     mv db.sqlite3.upload db.sqlite3
     touch /var/www/moabiblio_pythonanywhere_com_wsgi.py'
shasum db.sqlite3 | cut -d' ' -f1 > db.sqlite3.live-sha
echo "Uploaded db.sqlite3 as the live database."
