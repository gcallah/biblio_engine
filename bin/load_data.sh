#!/bin/bash
# Run every data loader against the local db.sqlite3. The loaders are
# idempotent, so a second run should report 0 added.
# Usage: bin/load_data.sh
set -e
cd "$(dirname "$0")/.."
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
