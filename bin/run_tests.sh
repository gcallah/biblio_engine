#!/bin/bash
# Run the test suite twice: the engine on its own, as a made-up site
# (mysite/settings_engine_test.py), then the engine and the Oakeshott
# site together under the real settings.
# Usage: bin/run_tests.sh [extra manage.py test args, used for both runs]
set -e
cd "$(dirname "$0")/.."
echo "== engine (made-up site)"
.venv/bin/python manage.py test berkeley \
    --settings=mysite.settings_engine_test "$@"
echo "== Oakeshott site"
.venv/bin/python manage.py test berkeley sites.oakeshott "$@"
