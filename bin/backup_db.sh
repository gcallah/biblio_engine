#!/bin/bash
# Copy db.sqlite3 to /tmp with a timestamp before changing data.
# Usage: bin/backup_db.sh [label]
set -e
cd "$(dirname "$0")/.."
dest="/tmp/db.sqlite3.${1:-backup}-$(date +%Y%m%d-%H%M%S)"
cp db.sqlite3 "$dest"
echo "Backed up db.sqlite3 to $dest"
