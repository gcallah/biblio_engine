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

    def test_pub_detail_review_of_only_for_reviews(self):
        url = f"/oakeshott/pub_detail/{self.book.id}/"
        self.assertNotIn("Review of:", self.page_text(url))
        review = self.pub("", 1950, pub_type="RVBY", authors=[self.mo],
                          review="Freedom", reviewed_names="M. Cranston")
        text = self.page_text(f"/oakeshott/pub_detail/{review.id}/")
        self.assertIn("Publication: Review of M. Cranston, Freedom", text)
        self.assertIn("<i>Freedom</i>, by M. Cranston", text)
        self.assertNotIn("Reprinted in:", text)
        review.reprinted_in.add(self.book)
        text = self.page_text(f"/oakeshott/pub_detail/{review.id}/")
        self.assertIn("Reprinted in:", text)
        self.assertIn(f'href="/oakeshott/pub_detail/{self.book.id}/"', text)
        text = self.page_text(url)
        self.assertIn("Reprints (1):", text)
        self.assertIn("Review of M. Cranston, Freedom", text)

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

    def test_person_detail_shows_affiliation(self):
        self.mo.affiliation = "London School of Economics"
        self.mo.save()
        text = self.page_text(f"/oakeshott/person_detail/{self.mo.id}/")
        self.assertIn("Affiliation:", text)
        self.assertIn("London School of Economics", text)

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
                         ["lname", "reviewed", "pub_type", "start_year",
                          "end_year",
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


class ListPunctuationTest(BiblioTestCase):
    """Comma-separated lists have no comma after the last item."""

    def setUp(self):
        super().setUp()
        self.mo = self.person("Michael", "Oakeshott")
        self.gg = self.person("Guy", "Griffith")
        self.both = self.pub("A Guide", 1936, authors=[self.mo, self.gg])
        self.solo = self.pub("Solo", 1940, authors=[self.mo])
        self.both.keywords.add(Keyword.objects.create(name="racing"),
                               Keyword.objects.create(name="wit"))

    def test_results_list(self):
        text = self.page_text("/oakeshott/publications/")
        self.assertIn(f'Oakeshott</a>, <a href="/oakeshott/person_detail/{self.gg.id}/">Griffith</a> </td>', text)
        self.assertIn(">Oakeshott</a> </td>", text)
        self.assertNotIn("Griffith,", text)
        self.assertNotIn("nbsp;>", text)

    def test_detail_and_edit_pages(self):
        for route in ("pub_detail", "edit_pub"):
            text = self.page_text(f"/oakeshott/{route}/{self.both.id}/")
            self.assertIn("Michael Oakeshott</a>, <a", text, route)
            self.assertIn("Guy Griffith</a> </td>", text, route)
            self.assertIn("racing, wit </td>", text, route)
            self.assertNotIn("nbsp;>", text, route)
