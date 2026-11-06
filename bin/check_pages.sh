#!/bin/bash
# Render the results page for each publication type and every export
# page from the local db.sqlite3, and report errors or broken citation
# punctuation (e.g. ", ." left by an empty field).
# Usage: bin/check_pages.sh
cd "$(dirname "$0")/.."
.venv/bin/python bin/check_pages.py
