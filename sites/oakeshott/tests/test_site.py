"""What the Oakeshott site adds to the engine: its About page, its
background picture and the redirects from its old /berkeley/ URLs."""
from berkeley.tests.helpers import BiblioTestCase


class OakeshottPagesTest(BiblioTestCase):
    def test_about_page_replaces_the_engines(self):
        resp = self.client.get("/oakeshott/about/")
        self.assertContains(resp, "About the Michael Oakeshott Bibliography")
        self.assertContains(resp, "Adnan Bin Hoq")

    def test_background_is_the_caius_gate(self):
        self.assertContains(
            self.client.get("/oakeshott/"),
            'url("/static/berkeley/img/caius-gate-of-honour.jpg")')


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
