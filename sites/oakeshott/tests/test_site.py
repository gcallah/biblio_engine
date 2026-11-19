"""What the Oakeshott site adds to the engine: its About page, its
background picture and the redirects from its old /berkeley/ URLs."""
from django.conf import settings
from django.contrib.staticfiles import finders

from berkeley.tests.helpers import BiblioTestCase


class OakeshottPagesTest(BiblioTestCase):
    def test_about_page_replaces_the_engines(self):
        resp = self.client.get("/oakeshott/about/")
        self.assertContains(resp, "About the Michael Oakeshott Bibliography")
        self.assertContains(resp, "Adnan Bin Hoq")

    def test_background_is_the_caius_gate(self):
        self.assertContains(
            self.client.get("/oakeshott/"),
            'url("/static/oakeshott/img/caius-gate-of-honour.jpg")')

    def test_default_look(self):
        """Oakeshott has no stylesheet of its own: the engine's look."""
        html = self.client.get("/oakeshott/").content.decode()
        self.assertEqual(html.count('rel="stylesheet" type="text/css"'), 1)

    def test_portrait_and_background_are_found(self):
        for key in ("portrait", "background"):
            self.assertTrue(finders.find(settings.BIBLIO_SITE[key]), key)


class OldUrlRedirectTest(BiblioTestCase):
    def test_berkeley_urls_redirect_permanently(self):
        resp = self.client.get("/berkeley/about/")
        self.assertEqual(resp.status_code, 301)
        self.assertEqual(resp["Location"], "/oakeshott/about/")

    def test_redirect_keeps_query_string(self):
        resp = self.client.get("/berkeley/publications/?lname=oake")
        self.assertEqual(resp.status_code, 301)
        self.assertEqual(resp["Location"],
                         "/oakeshott/publications/?lname=oake")
