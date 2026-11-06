"""The Django admin pages for the bibliography."""
from django.contrib.auth.models import User

from berkeley.models import Authorship

from .helpers import BiblioTestCase

MODELS = ("address", "adminemail", "institution", "journal", "keyword",
          "person", "publication", "publisher", "site", "subject")


class AdminTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        User.objects.create_superuser("admin", "a@example.com", "pw")
        self.client.login(username="admin", password="pw")
        self.mo = self.person("Michael", "Oakeshott")
        self.pub_ = self.pub("Notebooks", 2014, pub_type="BKBY",
                             authors=[self.mo])

    def test_changelists_load(self):
        for model in MODELS:
            url = f"/admin/berkeley/{model}/"
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_add_pages_load(self):
        for model in MODELS:
            url = f"/admin/berkeley/{model}/add/"
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_address_with_empty_fields_lists(self):
        from berkeley.models import Address
        Address.objects.create(street=None, city="London", country=None)
        resp = self.client.get("/admin/berkeley/address/")
        self.assertContains(resp, "London")

    def test_publication_has_author_inline(self):
        resp = self.client.get(
            f"/admin/berkeley/publication/{self.pub_.id}/change/")
        self.assertContains(resp, "authorship_set-0-position")
        self.assertContains(resp, "authorship_set-0-person")

    def test_set_author_order_through_admin(self):
        berlin = self.person("Isaiah", "Berlin")
        url = f"/admin/berkeley/publication/{self.pub_.id}/change/"
        form = self.client.get(url).context["adminform"].form
        data = {k: v for k, v in form.initial.items() if v is not None}
        data.update({
            "title": "Notebooks", "year": 2014, "pub_type": "BKBY",
            "subject": self.unknown.id,
            "authorship_set-TOTAL_FORMS": 2,
            "authorship_set-INITIAL_FORMS": 1,
            "authorship_set-0-id": self.pub_.authorship_set.get().id,
            "authorship_set-0-publication": self.pub_.id,
            "authorship_set-0-person": self.mo.id,
            "authorship_set-0-position": 2,
            "authorship_set-1-publication": self.pub_.id,
            "authorship_set-1-person": berlin.id,
            "authorship_set-1-position": 1,
            "editorship_set-TOTAL_FORMS": 0,
            "editorship_set-INITIAL_FORMS": 0,
        })
        for field in ("editors", "translators", "reviewees", "keywords"):
            data.pop(field, None)
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302, getattr(resp, "context", None)
                         and resp.context.get("errors"))
        self.pub_.refresh_from_db()
        self.assertEqual(self.pub_.ordered_authors(), [berlin, self.mo])

    def test_set_editor_order_through_admin(self):
        nardin = self.person("Terry", "Nardin")
        osullivan = self.person("Luke", "O'Sullivan")
        url = f"/admin/berkeley/publication/{self.pub_.id}/change/"
        form = self.client.get(url).context["adminform"].form
        data = {k: v for k, v in form.initial.items() if v is not None}
        data.update({
            "title": "Notebooks", "year": 2014, "pub_type": "BKBY",
            "subject": self.unknown.id,
            "authorship_set-TOTAL_FORMS": 1,
            "authorship_set-INITIAL_FORMS": 1,
            "authorship_set-0-id": self.pub_.authorship_set.get().id,
            "authorship_set-0-publication": self.pub_.id,
            "authorship_set-0-person": self.mo.id,
            "authorship_set-0-position": 1,
            "editorship_set-TOTAL_FORMS": 2,
            "editorship_set-INITIAL_FORMS": 0,
            "editorship_set-0-publication": self.pub_.id,
            "editorship_set-0-person": osullivan.id,
            "editorship_set-0-position": 2,
            "editorship_set-1-publication": self.pub_.id,
            "editorship_set-1-person": nardin.id,
            "editorship_set-1-position": 1,
        })
        for field in ("editors", "translators", "reviewees", "keywords"):
            data.pop(field, None)
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(self.pub_.ordered_editors(), [nardin, osullivan])

    def test_admin_requires_login(self):
        self.client.logout()
        resp = self.client.get("/admin/berkeley/publication/")
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/admin/login/", resp["Location"])
