"""Editor logins: the Login link, the login page, the edit pencils that
logged-in editors see, and the add_editor command."""
import re
from io import StringIO

from django.contrib.auth.models import User
from django.core.management import call_command

from berkeley.models import Address, Journal, Publisher

from .helpers import BLANK_QUERY, PUBS_URL, BiblioTestCase

PENCIL = 'class="edit-pencil"'


class LoginTestCase(BiblioTestCase):
    def setUp(self):
        super().setUp()
        call_command("add_editor", "editor", password="pw", stdout=StringIO())
        self.mo = self.person("Michael", "Oakeshott")
        self.methuen = Publisher.objects.create(
            name="Methuen", address=Address.objects.create(city="London"))
        self.journal = Journal.objects.create(name="Political Studies")
        self.book = self.pub("Rationalism in Politics", 1962, pub_type="BKBY",
                             authors=[self.mo], publisher=self.methuen,
                             abstract="Essays.")
        self.article = self.pub("On Being Conservative", 1956,
                                pub_type="SWBY", authors=[self.mo],
                                journal=self.journal)

    def login(self):
        self.assertTrue(self.client.login(username="editor", password="pw"))

    def results(self):
        return self.client.get(PUBS_URL, BLANK_QUERY).content.decode()


class AnonymousTest(LoginTestCase):
    def test_menu_has_login_link(self):
        html = self.client.get("/oakeshott/").content.decode()
        self.assertIn('href="/oakeshott/login/?next=/oakeshott/">Login</a>',
                      html)
        self.assertNotIn("Log out", html)

    def test_no_pencils(self):
        self.assertNotIn(PENCIL, self.results())
        html = self.client.get(
            f"/oakeshott/pub_detail/{self.book.id}/").content.decode()
        self.assertNotIn(PENCIL, html)

    def test_login_page(self):
        resp = self.client.get("/oakeshott/login/")
        self.assertContains(resp, "Editor login")
        # no "next" loop back to the login page itself
        self.assertContains(resp, 'href="/oakeshott/login/">Login</a>')

    def test_bad_password(self):
        resp = self.client.post("/oakeshott/login/",
                                {"username": "editor", "password": "no"})
        self.assertContains(resp, "didn't match")

    def test_logging_in_returns_to_the_page(self):
        resp = self.client.post("/oakeshott/login/",
                                {"username": "editor", "password": "pw",
                                 "next": "/oakeshott/about/"})
        self.assertRedirects(resp, "/oakeshott/about/",
                             fetch_redirect_response=False)
        html = self.client.get("/oakeshott/about/").content.decode()
        self.assertIn("Log out", html)
        self.assertNotIn(">Login</a>", html)


class EditorTest(LoginTestCase):
    def setUp(self):
        super().setUp()
        self.login()

    def test_pencil_on_publication_page(self):
        html = self.client.get(
            f"/oakeshott/pub_detail/{self.book.id}/").content.decode()
        self.assertIn(f'href="/admin/berkeley/publication/{self.book.id}'
                      '/change/" title="Edit this publication"', html)

    def test_pencils_in_popups(self):
        html = self.results()
        for model, obj in (("person", self.mo), ("journal", self.journal),
                           ("publisher", self.methuen),
                           ("publication", self.book)):
            self.assertIn(f'href="/admin/berkeley/{model}/{obj.id}/change/"',
                          html, model)

    def test_pencils_on_detail_pages(self):
        for route, model, obj in (("person_detail", "person", self.mo),
                                  ("journal_detail", "journal", self.journal),
                                  ("publisher_detail", "publisher",
                                   self.methuen)):
            html = self.client.get(
                f"/oakeshott/{route}/{obj.id}/").content.decode()
            self.assertIn(f'href="/admin/berkeley/{model}/{obj.id}/change/"',
                          html, route)

    def test_edit_pub_goes_to_admin(self):
        resp = self.client.get(f"/oakeshott/edit_pub/{self.book.id}/")
        self.assertRedirects(
            resp, f"/admin/berkeley/publication/{self.book.id}/change/")

    def test_editor_can_open_every_edit_page(self):
        for model, obj in (("publication", self.book), ("person", self.mo),
                           ("journal", self.journal),
                           ("publisher", self.methuen)):
            url = f"/admin/berkeley/{model}/{obj.id}/change/"
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200, url)
            # "View on site" leads back to the record's page
            link = re.search(r'href="(/admin/r/[^"]+)" class="viewsitelink"',
                             resp.content.decode())
            self.assertTrue(link, url)
            self.assertTrue(self.client.get(link.group(1))["Location"]
                            .endswith(obj.get_absolute_url()), url)

    def test_admin_autocomplete_searches_people(self):
        resp = self.client.get("/admin/autocomplete/", {
            "term": "Oake", "app_label": "berkeley",
            "model_name": "authorship", "field_name": "person"})
        self.assertContains(resp, "Oakeshott")

    def test_log_out(self):
        resp = self.client.post("/oakeshott/logout/")
        self.assertRedirects(resp, "/oakeshott/",
                             fetch_redirect_response=False)
        self.assertNotIn(PENCIL, self.results())


class AddEditorTest(BiblioTestCase):
    def test_creates_an_editor_who_can_edit_everything(self):
        out = StringIO()
        call_command("add_editor", "ann", password="s3cret",
                     email="ann@example.com", stdout=out)
        self.assertIn("Created editor 'ann'", out.getvalue())
        user = User.objects.get(username="ann")
        self.assertTrue(user.is_staff and user.is_superuser)
        self.assertEqual(user.email, "ann@example.com")
        self.assertTrue(user.check_password("s3cret"))

    def test_rerun_resets_password(self):
        call_command("add_editor", "ann", password="one", stdout=StringIO())
        out = StringIO()
        call_command("add_editor", "ann", password="two", stdout=out)
        self.assertIn("Updated editor 'ann'", out.getvalue())
        self.assertTrue(User.objects.get(username="ann").check_password("two"))
        self.assertEqual(User.objects.count(), 1)
