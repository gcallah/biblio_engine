"""The index page, an entry's index terms, and the possible index terms
on the editors' to-do page."""
from berkeley.models import IndexTerm, PossibleIndexTerm

from .helpers import ROOT, squash
from .test_login import LoginTestCase

INDEX_URL = f"{ROOT}index/"


class IndexTestCase(LoginTestCase):
    def term(self, name, *entries):
        term = IndexTerm.objects.create(name=name)
        term.entries.set(entries)
        return term


class IndexPageTest(IndexTestCase):
    def test_empty_index(self):
        resp = self.client.get(INDEX_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "There is no index yet.")

    def test_menu_links_to_it_once_it_has_terms(self):
        html = self.client.get(ROOT).content.decode()
        self.assertNotIn(f'href="{INDEX_URL}"', html)
        self.term("rationalism", self.book)
        html = self.client.get(ROOT).content.decode()
        self.assertEqual(html.count(f'href="{INDEX_URL}">Index</a>'), 2)

    def test_terms_a_to_z_with_their_entries(self):
        self.term("rationalism", self.book, self.article)
        self.term("Hobbes, Thomas", self.book)
        self.term("conservatism", self.article)
        html = squash(self.client.get(INDEX_URL).content.decode())
        # letters, then terms, ignoring case
        self.assertLess(html.index('id="letter-C"'),
                        html.index('id="letter-H"'))
        self.assertLess(html.index('id="hobbes-thomas"'),
                        html.index('id="rationalism"'))
        self.assertIn('<a href="#letter-R">R</a>', html)
        # entries oldest first, one per line, labelled with surnames and year
        start = html.index('id="rationalism"')
        part = html[start:html.index("</dd>", start)]
        self.assertIn(f'href="{ROOT}pub_detail/{self.article.id}/">'
                      "On Being Conservative (Oakeshott, 1956)</a></li>", part)
        self.assertLess(part.index("On Being Conservative"),
                        part.index("Rationalism in Politics (Oakeshott, 1962)"))

    def test_no_pencils_for_visitors(self):
        self.term("rationalism", self.book)
        self.assertNotContains(self.client.get(INDEX_URL), "edit-pencil")
        self.login()
        self.assertContains(self.client.get(INDEX_URL), "edit-pencil")

    def test_entry_page_links_to_its_terms(self):
        self.term("civil association", self.book)
        html = self.client.get(
            f"{ROOT}pub_detail/{self.book.id}/").content.decode()
        self.assertIn("In the index:", html)
        self.assertIn(f'href="{INDEX_URL}#civil-association">'
                      "civil association</a>", html)
        html = self.client.get(
            f"{ROOT}pub_detail/{self.article.id}/").content.decode()
        self.assertNotIn("In the index:", html)


class PossibleIndexTermsTest(IndexTestCase):
    def setUp(self):
        super().setUp()
        self.login()
        self.term("conservatism", self.book)
        maybe = PossibleIndexTerm.objects.create(
            name="conservatism", details="Calls him conservative.")
        maybe.entries.set([self.article])
        PossibleIndexTerm.objects.create(name="experience",
                                         details="Too broad?")
        PossibleIndexTerm.objects.create(name="settled one", settled=True)

    def test_listed_on_the_todo_page(self):
        html = squash(self.client.get(f"{ROOT}todo/").content.decode())
        self.assertIn("<h3>Possible index terms</h3>", html)
        self.assertIn("<strong>conservatism</strong> (in the index: "
                      f'<a href="{INDEX_URL}#conservatism">see it</a>)', html)
        self.assertIn("<strong>experience</strong> (not in the index)", html)
        self.assertIn("Possible entries (1)", html)
        self.assertIn("On Being Conservative (Oakeshott, 1956)", html)
        self.assertNotIn("settled one", html)

    def test_admin_pages(self):
        for model in ("indexterm", "possibleindexterm"):
            for page in ("", "add/"):
                resp = self.client.get(f"/admin/berkeley/{model}/{page}")
                self.assertEqual(resp.status_code, 200, (model, page))


class ChooseEntriesTest(IndexTestCase):
    """An index term's entries are tick boxes: those under it, ticked,
    and those its possible index term suggests, not."""

    def setUp(self):
        super().setUp()
        self.login()
        self.conservatism = self.term("conservatism", self.book)
        self.maybe = PossibleIndexTerm.objects.create(name="conservatism")
        self.maybe.entries.set([self.article])
        self.url = (f"/admin/berkeley/indexterm/{self.conservatism.id}/"
                    "change/")

    def post(self, url, **data):
        resp = self.client.post(url, {"name": "conservatism", **data})
        self.assertEqual(resp.status_code, 302)

    def test_tick_boxes(self):
        html = self.client.get(self.url).content.decode()
        self.assertIn(f'type="checkbox" name="entries" value="{self.book.id}"'
                      , html)
        self.assertIn("Possible: On Being Conservative (Oakeshott, 1956)",
                      html)
        self.assertIn("Settled", html)
        # only these two, not every entry
        self.assertEqual(html.count('type="checkbox" name="entries"'), 2)

    def test_ticking_and_unticking(self):
        self.post(self.url, entries=[self.article.id], settle="on")
        self.assertEqual(list(self.conservatism.entries.all()),
                         [self.article])
        self.maybe.refresh_from_db()
        self.assertTrue(self.maybe.settled)

    def test_left_unsettled(self):
        self.post(self.url, entries=[self.book.id, self.article.id])
        self.assertEqual(self.conservatism.entries.count(), 2)
        self.maybe.refresh_from_db()
        self.assertFalse(self.maybe.settled)

    def test_other_entries_to_add(self):
        other = self.pub("Another", 1970)
        self.post(self.url, entries=[self.book.id], more_entries=[other.id])
        self.assertEqual(set(self.conservatism.entries.all()),
                         {self.book, other})

    def test_a_new_term_from_the_todo_page(self):
        maybe = PossibleIndexTerm.objects.create(name="experience")
        maybe.entries.set([self.book])
        html = self.client.get(f"{ROOT}todo/").content.decode()
        self.assertIn('href="/admin/berkeley/indexterm/add/?name=experience"',
                      html)
        self.assertIn('href="/admin/berkeley/indexterm/'
                      f'{self.conservatism.id}/change/"', html)
        url = "/admin/berkeley/indexterm/add/?name=experience"
        html = self.client.get(url).content.decode()
        self.assertEqual(html.count('type="checkbox" name="entries"'), 1)
        self.client.post(url, {"name": "experience",
                               "entries": [self.book.id], "settle": "on"})
        term = IndexTerm.objects.get(name="experience")
        self.assertEqual(list(term.entries.all()), [self.book])
        maybe.refresh_from_db()
        self.assertTrue(maybe.settled)
