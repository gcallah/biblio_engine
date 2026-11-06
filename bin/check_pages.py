"""Render key pages from the local db.sqlite3 with Django's test client
and report problems: one results page per publication type, and every
export page, checked for broken citation punctuation.

Run through bin/check_pages.sh.
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django  # noqa: E402
django.setup()

from django.test import Client  # noqa: E402
from django.test.utils import setup_test_environment  # noqa: E402

from berkeley.models import Publication, TYPE_CHOICES  # noqa: E402

# punctuation left behind when a citation field is empty
BROKEN = re.compile(r"</i>,\s*\.|,\s*\.|\(\s*\)|:\s*\.|\.\s*\.(?!\.)")


def text(resp):
    return re.sub(r"\s+", " ", resp.content.decode())


def main():
    setup_test_environment()
    client = Client()
    problems = 0
    for code, label in TYPE_CHOICES:
        if not code:
            continue
        resp = client.get(f"/oakeshott/publications/?pub_type={code}",
                          follow=True, secure=True)
        count = len(resp.context["pub_list"]) if resp.context else 0
        print(f"results {code:4} {resp.status_code}  {count:4}  {label}")
        problems += resp.status_code != 200
    for pub in Publication.objects.all():
        resp = client.get(f"/oakeshott/export/{pub.id}/", follow=True,
                          secure=True)
        page = text(resp)
        body = page[page.find("APA:"):page.find("</table>")]
        bad = BROKEN.findall(re.sub(r"<[^>]+>", "", body))
        if resp.status_code != 200 or bad:
            problems += 1
            print(f"export {pub.id} {resp.status_code} {pub.pub_type} "
                  f"{pub.title[:60]!r} {bad}")
    print(f"{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
