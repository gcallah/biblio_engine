"""Shared fixtures for the berkeley test suite."""
import re

from django.test import TestCase

from berkeley.models import (
    Address, Authorship, Journal, Keyword, Person, Publication, Publisher,
    Subject, UNKNOWN_ID,
)

PUBS_URL = "/oakeshott/publications/"
BLANK_QUERY = {"lname": "", "reviewed": "", "pub_type": "", "start_year": "", "end_year": "",
               "subject": "", "keyword1": ""}


def squash(html):
    """Collapse runs of whitespace so rendered citations are easy to match."""
    return re.sub(r"\s+", " ", html)


class BiblioTestCase(TestCase):
    """TestCase with the 'Unknown' subject every Publication defaults to."""

    def setUp(self):
        self.unknown = Subject.objects.create(id=UNKNOWN_ID, name="Unknown")

    # --- factories ---------------------------------------------------------
    def person(self, fname, lname, **kw):
        return Person.objects.create(fname=fname, lname=lname, **kw)

    def pub(self, title="Untitled", year=1950, authors=(), **kw):
        pub = Publication.objects.create(title=title, year=year, **kw)
        for pos, author in enumerate(authors, start=1):
            Authorship.objects.create(publication=pub, person=author,
                                      position=pos)
        return pub

    # --- requests ----------------------------------------------------------
    def search(self, **params):
        resp = self.client.get(PUBS_URL, {**BLANK_QUERY, **params})
        self.assertEqual(resp.status_code, 200)
        return resp

    def results(self, **params):
        return list(self.search(**params).context["pub_list"])

    def page_text(self, url):
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        return squash(resp.content.decode())
