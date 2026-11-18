#!/bin/bash
# One-off setup of a new site on its own PythonAnywhere account, before
# its first deploy (deploy.sh expects all of this to be there already).
# Run it from your machine:
#
#   bin/setup_pa_site.sh <account> <settings module> <password> <API token>
#   e.g. bin/setup_pa_site.sh voegelin mysite.settings_voegelin \
#            "$VOEGELIN_PWD" "$VOEGELIN_API"
#
# On the server it:
#   - moves an existing ~/mysite that is not this repo aside (the Flask
#     demo PythonAnywhere creates) and clones the repo to ~/mysite;
#   - makes the virtualenv ~/.virtualenvs/biblio (Python 3.12, as CI and
#     the Oakeshott server use) and installs the requirements;
#   - sets DJANGO_SETTINGS_MODULE in ~/.bashrc, so manage.py there is
#     this site's;
#   - migrates a new, empty database and adds subject 9, "Uncategorized",
#     which every entry defaults to;
#   - collects the static files and writes the Django WSGI file.
# Then, through the API, it points the web app at Python 3.12 and the
# virtualenv, maps /static/ to ~/mysite/static_collected and reloads.
#
# It can be run again: each step skips what is already done. It does not
# make a login; do that in a PythonAnywhere console with
#   cd ~/mysite && workon biblio && python manage.py createsuperuser
set -e

PA_USER=$1
SETTINGS=$2
PWD_=$3
API=$4
[ -n "$API" ] || { echo "usage: $0 <account> <settings> <pwd> <api>"; exit 1; }
REPO=https://github.com/gcallah/biblio_engine.git
DOMAIN=$PA_USER.pythonanywhere.com
API_URL=https://www.pythonanywhere.com/api/v0/user/$PA_USER/webapps/$DOMAIN

echo "== setting up $DOMAIN ($SETTINGS)"
sshpass -p "$PWD_" ssh -T -o "StrictHostKeyChecking no" \
    $PA_USER@ssh.pythonanywhere.com \
    "PA_USER='$PA_USER' SETTINGS='$SETTINGS' REPO='$REPO' bash -s" << 'EOF'
set -e
cd ~
if [ -d mysite ] && [ ! -d mysite/.git ]; then
    aside=mysite_before_biblio_$(date +%Y%m%d-%H%M%S)
    mv mysite "$aside"
    echo "Moved the old ~/mysite to ~/$aside"
fi
[ -d mysite ] || git clone -q "$REPO" mysite
cd mysite
git pull -q origin master

if [ ! -x ~/.virtualenvs/biblio/bin/python ]; then
    python3.12 -m venv ~/.virtualenvs/biblio
fi
source ~/.virtualenvs/biblio/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements/requirements.txt

line="export DJANGO_SETTINGS_MODULE=$SETTINGS"
grep -qxF "$line" ~/.bashrc || echo "$line" >> ~/.bashrc
export DJANGO_SETTINGS_MODULE=$SETTINGS

python manage.py migrate --noinput -v0
python manage.py shell -c "
from berkeley.models import Subject, UNKNOWN_ID
s, made = Subject.objects.get_or_create(id=UNKNOWN_ID,
                                        defaults={'name': 'Uncategorized'})
print('Subject', s.id, s.name, '(added)' if made else '(already there)')"
python manage.py collectstatic --noinput -v0

cat > /var/www/${PA_USER}_pythonanywhere_com_wsgi.py << WSGI
# Django, for the site whose settings are $SETTINGS
# (written by bin/setup_pa_site.sh)
import os
import sys

path = "/home/$PA_USER/mysite"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ["DJANGO_SETTINGS_MODULE"] = "$SETTINGS"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
WSGI
echo "Wrote the WSGI file"
python manage.py check
EOF

auth="Authorization: Token $API"
echo "== web app: Python 3.12, virtualenv, /static/"
# two calls: the API checks the virtualenv against the version already set
curl -sf -X PATCH -H "$auth" "$API_URL/" -d python_version=3.12 > /dev/null
curl -sf -X PATCH -H "$auth" "$API_URL/" \
     -d virtualenv_path=/home/$PA_USER/.virtualenvs/biblio > /dev/null
if ! curl -sf -H "$auth" "$API_URL/static_files/" | grep -q '"/static/"'; then
    curl -sf -X POST -H "$auth" "$API_URL/static_files/" \
         -d url=/static/ -d path=/home/$PA_USER/mysite/static_collected \
         > /dev/null
fi
curl -sf -X POST -H "$auth" "$API_URL/reload/" > /dev/null
echo "== done: https://$DOMAIN/"
