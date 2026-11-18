"""
Settings for the Eric Voegelin bibliography
(voegelin.pythonanywhere.com/voegelin/): the shared settings in
settings_base.py plus what is particular to this site. On its server the
WSGI file and the shell set DJANGO_SETTINGS_MODULE=mysite.settings_voegelin;
elsewhere pass --settings=mysite.settings_voegelin, and use a database of
its own (not an Oakeshott db.sqlite3).
"""
from .settings_base import *  # noqa: F401,F403

ALLOWED_HOSTS = ["voegelin.pythonanywhere.com", "127.0.0.1", "0.0.0.0"]

# the site comes before the engine, so its templates win
INSTALLED_APPS = ["sites.voegelin"] + INSTALLED_APPS  # noqa: F405

BIBLIO_URL_PREFIX = "voegelin"
BIBLIO_OLD_URL_PREFIXES = ()

# See mysite/settings.py for what each key does. No background picture
# yet.
BIBLIO_SITE = {
    "name": "Eric Voegelin",
    "short_name": "Voegelin",
    "dates": "1901 – 1985",
    # Copyrighted; used, as on Wikipedia, under fair use (a small copy, to
    # identify the subject of a non-commercial scholarly bibliography).
    # Source: https://en.wikipedia.org/wiki/File:Eric_Voegelin.jpg, from
    # voegelinview.com. If the rights holder objects, remove it (the
    # site works without a portrait).
    "portrait": "voegelin/img/voegelin.jpg",
    "portrait_version": "1",
    "portrait_alt": "Portrait of Eric Voegelin",
    "credits": "Portrait: via VoegelinView (voegelinview.com), used "
               "under fair use.",
    "pub_type_labels": {},
}
