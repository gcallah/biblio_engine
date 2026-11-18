#!/bin/bash
# Run the test suite three times: the engine on its own, as a made-up
# site (mysite/settings_engine_test.py), then the engine with each real
# site (Oakeshott, Voegelin) under that site's settings.
# Usage: bin/run_tests.sh [extra manage.py test args, used for both runs]
set -e
cd "$(dirname "$0")/.."
echo "== engine (made-up site)"
.venv/bin/python manage.py test berkeley \
    --settings=mysite.settings_engine_test "$@"
echo "== Oakeshott site"
.venv/bin/python manage.py test berkeley sites.oakeshott "$@"
echo "== Voegelin site"
.venv/bin/python manage.py test berkeley sites.voegelin \
    --settings=mysite.settings_voegelin "$@"
