"""Every page renders, missing objects 404, and old URLs redirect."""
from berkeley.forms import SearchForm
from berkeley.models import (
    AdminEmail, Journal, Keyword, Publisher, Site, TYPE_CHOICES,
)

from .helpers import BiblioTestCase


class PagesRenderTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.mo = self.person("Michael", "Oakeshott", yob=1901, yod=1990)
        self.publisher = Publisher.objects.create(name="Methuen")
        self.journal = Journal.objects.create(name="Cambridge Journal",
                                              publisher=self.publisher)
        self.kw = Keyword.objects.create(name="conversation")
        self.book = self.pub("Rationalism in Politics", 1962, pub_type="BKBY",
                             authors=[self.mo], publisher=self.publisher,
                             journal=self.journal, abstract="Essays.")
        self.book.keywords.add(self.kw)

    def test_static_pages(self):
        for url in ("/oakeshott/", "/oakeshott/about/", "/oakeshott/about",
                    "/oakeshott/feedback/", "/oakeshott/publications/"):
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_pub_detail(self):
        text = self.page_text(f"/oakeshott/pub_detail/{self.book.id}/")
        for expected in ("Rationalism in Politics", "Michael Oakeshott",
                         "1962", "Methuen", "Cambridge Journal",
                         "conversation", "Essays.",
                         f'href="/oakeshott/person_detail/{self.mo.id}/"',
                         f'href="/oakeshott/export/{self.book.id}/"'):
            self.assertIn(expected, text)

    def test_pub_detail_review_link_only_when_present(self):
        url = f"/oakeshott/pub_detail/{self.book.id}/"
        self.assertNotIn("Review of:", self.page_text(url))
        self.book.review = "https://example.com/review"
        self.book.save()
        text = self.page_text(url)
        self.assertIn('href="https://example.com/review"', text)
        self.assertIn("Review of: Rationalism in Politics", text)

    def test_edit_pub(self):
        text = self.page_text(f"/oakeshott/edit_pub/{self.book.id}/")
        self.assertIn("Edit Publication: Rationalism in Politics", text)
        self.assertIn("Michael Oakeshott", text)

    def test_person_detail(self):
        text = self.page_text(f"/oakeshott/person_detail/{self.mo.id}/")
        self.assertIn("Person: Michael Oakeshott", text)
        self.assertIn("1901", text)
        self.assertIn("1990", text)
        for gone in ("Institution:", "Department:", "Rank:"):
            self.assertNotIn(gone, text)

    def test_journal_detail(self):
        text = self.page_text(f"/oakeshott/journal_detail/{self.journal.id}/")
        self.assertIn("Journal: Cambridge Journal", text)
        self.assertIn(f'href="/oakeshott/publisher_detail/{self.publisher.id}/"',
                      text)

    def test_publisher_detail(self):
        text = self.page_text(f"/oakeshott/publisher_detail/{self.publisher.id}/")
        self.assertIn("Publisher: Methuen", text)

    def test_missing_objects_are_404(self):
        for route in ("pub_detail", "edit_pub", "export", "person_detail",
                      "journal_detail", "publisher_detail"):
            url = f"/oakeshott/{route}/9999/"
            self.assertEqual(self.client.get(url).status_code, 404, url)

    def test_non_numeric_id_is_404(self):
        self.assertEqual(self.client.get("/oakeshott/pub_detail/abc/").status_code,
                         404)


class SiteHeaderTest(BiblioTestCase):
    def test_default_header(self):
        self.assertContains(self.client.get("/oakeshott/"),
                            "Bibliography Search")

    def test_header_from_site_record(self):
        Site.objects.create(name="biblio", header="Oakeshott Bibliography")
        resp = self.client.get("/oakeshott/about/")
        self.assertContains(resp, "Oakeshott Bibliography")
        self.assertNotContains(resp, "Bibliography Search")


class FeedbackTest(BiblioTestCase):
    def test_mailto_lists_all_admin_emails(self):
        AdminEmail.objects.create(email_addr="a@example.com")
        AdminEmail.objects.create(email_addr="b@example.com")
        self.assertContains(self.client.get("/oakeshott/feedback/"),
                            'action="mailto:a@example.com,b@example.com"')

    def test_no_admin_emails(self):
        self.assertContains(self.client.get("/oakeshott/feedback/"),
                            'action="mailto:"')


class OldUrlRedirectTest(BiblioTestCase):
    def test_berkeley_urls_redirect_permanently(self):
        resp = self.client.get("/berkeley/about/")
        self.assertEqual(resp.status_code, 301)
        self.assertEqual(resp["Location"], "/oakeshott/about/")

    def test_redirect_keeps_query_string(self):
        resp = self.client.get("/berkeley/publications/?lname=oake")
        self.assertEqual(resp.status_code, 301)
        self.assertEqual(resp["Location"], "/oakeshott/publications/?lname=oake")


class SearchFormTest(BiblioTestCase):
    def test_form_fields_in_order(self):
        self.assertEqual(list(SearchForm().fields),
                         ["lname", "pub_type", "start_year", "end_year",
                          "subject", "keyword1"])

    def test_labels(self):
        form = SearchForm()
        self.assertEqual(form["lname"].label, "Author last name:")
        self.assertEqual(form["start_year"].label, "From year:")
        self.assertEqual(form["end_year"].label, "To year:")

    def test_search_page_renders_every_field_and_type(self):
        resp = self.client.get("/oakeshott/")
        for name in SearchForm().fields:
            self.assertContains(resp, f'name="{name}"')
        for code, label in TYPE_CHOICES:
            if code:
                self.assertContains(resp, f'value="{code}"')
                self.assertContains(resp, label)
        self.assertContains(resp, 'action="/oakeshott/publications"')

    def test_no_field_is_required_in_the_browser(self):
        self.assertNotContains(self.client.get("/oakeshott/"), "required")

    def test_keywords_listed_case_insensitively(self):
        for name in ("beta", "Alpha", "gamma"):
            Keyword.objects.create(name=name)
        names = [kw.name for kw in SearchForm().fields["keyword1"].queryset]
        self.assertEqual(names, ["Alpha", "beta", "gamma"])

    def test_new_keywords_appear_without_restart(self):
        self.assertEqual(SearchForm().fields["keyword1"].queryset.count(), 0)
        Keyword.objects.create(name="new")
        self.assertEqual(SearchForm().fields["keyword1"].queryset.count(), 1)
