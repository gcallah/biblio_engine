"""The Voegelin site: the engine's pages under /voegelin/, about Voegelin.

    python manage.py test berkeley sites.voegelin \
        --settings=mysite.settings_voegelin
"""
from django.conf import settings
from django.contrib.staticfiles import finders

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

    def test_portrait_and_credit(self):
        resp = self.client.get("/voegelin/")
        self.assertContains(resp, 'src="/static/voegelin/img/voegelin.jpg')
        self.assertContains(resp, 'alt="Portrait of Eric Voegelin"')
        self.assertContains(resp, "used under fair use")
        self.assertTrue(finders.find(settings.BIBLIO_SITE["portrait"]))

    def test_background_is_the_wilderness(self):
        resp = self.client.get("/voegelin/")
        self.assertContains(
            resp,
            'url("/static/voegelin/img/israelites-in-the-wilderness.jpg")')
        self.assertContains(resp, "Pillar of Clouds")
        self.assertTrue(finders.find(settings.BIBLIO_SITE["background"]))

    def test_no_oakeshott_urls(self):
        self.assertEqual(self.client.get("/oakeshott/").status_code, 404)
        self.assertEqual(self.client.get("/berkeley/").status_code, 404)
