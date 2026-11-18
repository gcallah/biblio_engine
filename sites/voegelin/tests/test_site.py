"""The Voegelin site: the engine's pages under /voegelin/, about Voegelin.

    python manage.py test berkeley sites.voegelin \
        --settings=mysite.settings_voegelin
"""
from berkeley.tests.helpers import BiblioTestCase


class VoegelinPagesTest(BiblioTestCase):
    def test_masthead(self):
        resp = self.client.get("/voegelin/")
        self.assertContains(resp, "Eric Voegelin")
        self.assertContains(resp, "1901 – 1985")
        self.assertNotContains(resp, "Oakeshott")

    def test_about_page_is_the_engines(self):
        resp = self.client.get("/voegelin/about/")
        self.assertContains(resp, "About the Eric Voegelin Bibliography")

    def test_no_portrait_until_one_is_chosen(self):
        self.assertNotContains(self.client.get("/voegelin/"),
                               'class="portrait"')

    def test_no_oakeshott_urls(self):
        self.assertEqual(self.client.get("/oakeshott/").status_code, 404)
        self.assertEqual(self.client.get("/berkeley/").status_code, 404)
