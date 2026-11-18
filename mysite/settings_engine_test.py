"""Settings for testing the engine on its own, as a made-up site that
shares nothing with Oakeshott: no sites.oakeshott app (so none of its
templates or commands), another URL prefix, and another subject. Engine
tests must pass under these settings as well as under each real site's.

    python manage.py test berkeley --settings=mysite.settings_engine_test
"""
from .settings import *  # noqa: F401,F403

INSTALLED_APPS = [app for app in INSTALLED_APPS  # noqa: F405
                  if not app.startswith("sites.")]

BIBLIO_URL_PREFIX = "testbib"
BIBLIO_OLD_URL_PREFIXES = ()

BIBLIO_SITE = {
    "name": "Jane Example",
    "short_name": "Example",
    "dates": "1900 – 1999",
    "portrait": "example/img/portrait.jpg",
    "portrait_version": "1",
    "portrait_alt": "Portrait of Jane Example",
    "credits": "Portrait: a made-up credit.",
    "pub_type_labels": {},
}
