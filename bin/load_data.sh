#!/bin/bash
# Run every data loader against the local db.sqlite3. The loaders are
# idempotent, so a second run should report 0 added.
# Usage: bin/load_data.sh
#
# The live database is now the master copy (editors change it on the
# site), so this is for building a database from scratch. Don't run it on
# a copy of the live database: a title an editor has corrected would be
# matched no longer and loaded again as a duplicate. For a new bulk load,
# run just the new loader on a copy from bin/pull_live_db.sh, check it,
# and upload it with bin/push_live_db.sh. It refuses to run on a database
# with editor logins unless FORCE=1.
set -e
cd "$(dirname "$0")/.."
if [ -z "${FORCE:-}" ] && [ -f db.sqlite3 ] && [ "$(sqlite3 db.sqlite3 \
        "select count(*) from auth_user" 2>/dev/null || echo 0)" != 0 ]; then
    echo "db.sqlite3 has editor logins, so it is a copy of the live" \
         "database: run just the new loader instead (or FORCE=1)." >&2
    exit 1
fi
for cmd in load_books_by_oakeshott load_books_about_oakeshott \
           load_short_works_about_oakeshott \
           load_short_works_by_oakeshott load_reviews_by_oakeshott \
           load_reviews_of_books_by_oakeshott \
           load_reviews_of_books_about_oakeshott \
           load_works_mentioning_oakeshott \
           load_abstracts load_keywords \
           load_author_info load_journal_info; do
    if [ -f "berkeley/management/commands/$cmd.py" ]; then
        echo "== $cmd"
        .venv/bin/python manage.py "$cmd"
    fi
done
