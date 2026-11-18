#!/bin/bash
# Run the Django test suite for the engine and the Oakeshott site.
# Usage: bin/run_tests.sh [extra manage.py test args]
set -e
cd "$(dirname "$0")/.."
.venv/bin/python manage.py test berkeley sites.oakeshott "$@"
