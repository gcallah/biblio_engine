"""
Settings for the Michael Oakeshott bibliography
(moabiblio.pythonanywhere.com/oakeshott/): the shared settings in
settings_base.py plus what is particular to this site. The server's WSGI
file and manage.py use this module (DJANGO_SETTINGS_MODULE=mysite.settings).
"""
from .settings_base import *  # noqa: F401,F403

ALLOWED_HOSTS = ["moabiblio.pythonanywhere.com",
                 "gcallah.pythonanywhere.com", "127.0.0.1", "0.0.0.0"]

# the site comes before the engine, so its templates win
INSTALLED_APPS = ["sites.oakeshott"] + INSTALLED_APPS  # noqa: F405

# Where the bibliography is mounted: /<BIBLIO_URL_PREFIX>/ (e.g.
# /oakeshott/). Links are built with reverse() and {% url %}, so this is
# the only place the prefix is set.
BIBLIO_URL_PREFIX = "oakeshott"
# Earlier prefixes, permanently redirected to the current one so old
# links keep working.
BIBLIO_OLD_URL_PREFIXES = ("berkeley",)

# Who this bibliography is about. The engine's templates, admin and
# publication-type labels read everything site-specific from here.
BIBLIO_SITE = {
    "name": "Michael Oakeshott",       # masthead, footer, admin
    "short_name": "Oakeshott",         # "Books by Oakeshott", ...
    "dates": "1901 \u2013 1990",
    "portrait": "oakeshott/img/oakeshott.jpg",   # a static file
    "portrait_version": "3",           # bump to refresh browser caches
    "portrait_alt": "Portrait of Michael Oakeshott in profile",
    # page background, a static file shown behind a dark tint (optional)
    "background": "oakeshott/img/caius-gate-of-honour.jpg",
    "credits": ("Background: the Gate of Honour, Gonville & Caius "
                "College, Cambridge (19th-century photograph, public "
                "domain). Portrait: LSE Library, no known copyright "
                "restrictions. Images via Wikimedia Commons."),
    # replacements for the standard type labels, by code, e.g.
    # {"MENT": "Works Discussing Oakeshott"}
    "pub_type_labels": {},
}
