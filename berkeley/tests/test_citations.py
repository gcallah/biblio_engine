"""The /export/<id>/ page: APA, MLA and Chicago citations for each type."""
from berkeley.models import Address, Journal, Publisher

from .helpers import BiblioTestCase


class CitationTestCase(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.mo = self.person("Michael", "Oakeshott")
        self.critic = self.person("Jane", "Critic")
        addr = Address.objects.create(city="London", province="England")
        self.methuen = Publisher.objects.create(name="Methuen", address=addr)
        self.journal = Journal.objects.create(name="Political Theory")

    def export(self, pub):
        return self.page_text(f"/oakeshott/export/{pub.id}/")


class BookCitationTest(CitationTestCase):
    def setUp(self):
        super().setUp()
        self.book = self.pub("Rationalism in Politics", 1962, pub_type="BKBY",
                             authors=[self.mo], publisher=self.methuen)

    def test_apa(self):
        self.assertIn("Oakeshott, M. (1962). <i>Rationalism in Politics</i>.",
                      self.export(self.book))
        self.assertIn("London, England: Methuen.", self.export(self.book))

    def test_mla_and_chicago(self):
        text = self.export(self.book)
        self.assertEqual(text.count(
            "<i>Rationalism in Politics</i>. London: Methuen, 1962."), 2)

    def test_books_about_use_book_format(self):
        about = self.pub("Oakeshott on Politics", 1990, pub_type="BKAB",
                         authors=[self.critic], publisher=self.methuen)
        self.assertIn("(1990). <i>Oakeshott on Politics</i>.", self.export(about))


class ShortWorkCitationTest(CitationTestCase):
    def setUp(self):
        super().setUp()
        self.article = self.pub(
            "The Tower of Babel", 1948, pub_type="SWBY", authors=[self.mo],
            journal=self.journal, volume="2", issue="3", pages="67-83")

    def test_apa(self):
        self.assertIn("(1948). The Tower of Babel. <i>Political Theory, 2</i>(3), 67-83.",
                      self.export(self.article))

    def test_mla(self):
        self.assertIn('"The Tower of Babel." <i>Political Theory</i> 1948: 67-83.',
                      self.export(self.article))

    def test_chicago(self):
        self.assertIn('"The Tower of Babel." <i>Political Theory</i>, 2, no. 3 (1948): 67-83.',
                      self.export(self.article))

    def test_apa_without_issue(self):
        self.article.issue = ""
        self.article.save()
        self.assertIn("<i>Political Theory, 2</i>, 67-83.",
                      self.export(self.article))

    def test_short_works_about_use_short_format(self):
        about = self.pub("On Oakeshott", 1991, pub_type="SWAB",
                         journal=self.journal, volume="9")
        self.assertIn('"On Oakeshott." <i>Political Theory</i>', self.export(about))


class MentioningCitationTest(CitationTestCase):
    def test_generic_format_has_authors_and_no_type_specific_parts(self):
        pub = self.pub("A Survey", 2001, pub_type="MENT", authors=[self.critic],
                       journal=self.journal)
        text = self.export(pub)
        self.assertIn("Critic, Jane.", text)
        self.assertNotIn("Political Theory", text)


class ReviewCitationTest(CitationTestCase):
    def setUp(self):
        super().setUp()
        self.book = self.pub("On Human Conduct", 1975, pub_type="BKBY",
                             authors=[self.mo])
        self.review = self.pub(
            "Conduct Considered", 1976, pub_type="RVAB", authors=[self.critic],
            pub_reviewed=self.book, journal=self.journal, volume="4",
            issue="2", month="May", pages="1-9")

    def test_apa(self):
        self.assertIn("(1976). Conduct Considered [Review of the book "
                      "<i>On Human Conduct</i>, by M. Oakeshott].",
                      self.export(self.review))

    def test_apa_author_initials(self):
        self.assertIn("Critic, J. (1976).", self.export(self.review))

    def test_mla_and_chicago(self):
        text = self.export(self.review)
        phrase = ('"Conduct Considered." Review of <i>On Human Conduct</i>, '
                  'by Michael Oakeshott. <i>Political Theory</i>')
        self.assertEqual(text.count(phrase), 2)
        self.assertIn("<i>Political Theory</i> May 1976: 1-9.", text)
        self.assertIn("<i>Political Theory</i> 4, no. 2 (1976): 1-9.", text)

    def test_reviews_by_oakeshott_use_review_format(self):
        self.review.pub_type = "RVBY"
        self.review.save()
        self.assertIn("[Review of the book", self.export(self.review))

    def test_untitled_review(self):
        self.review.title = ""
        self.review.save()
        text = self.export(self.review)
        self.assertIn("(1976). [Review of the book <i>On Human Conduct</i>", text)
        self.assertNotIn('""', text)

    def test_untitled_review_without_reviewed_book(self):
        self.review.title = ""
        self.review.pub_reviewed = None
        self.review.save()
        text = self.export(self.review)
        self.assertNotIn("Review of", text)
        self.assertNotIn('""', text)

    def test_reviewed_book_without_authors(self):
        self.book.authorship_set.all().delete()
        text = self.export(self.review)
        self.assertIn("[Review of the book <i>On Human Conduct</i>].", text)
        self.assertNotIn(", by", text)


class CitationAuthorListTest(CitationTestCase):
    def setUp(self):
        super().setUp()
        self.amy = self.person("Amy", "Alpha")
        self.zed = self.person("Zed", "Zulu")

    def test_authors_in_title_page_order_in_every_style(self):
        pub = self.pub("Joint", 1960, pub_type="BKBY",
                       authors=[self.zed, self.amy], publisher=self.methuen)
        text = self.export(pub)
        for style in ("APA:", "MLA:", "Chicago:"):
            section = text[text.index(style):]
            self.assertLess(section.index("Zulu"), section.index("Alpha"), style)

    def test_two_authors_on_export_page(self):
        pub = self.pub("Joint", 1960, pub_type="BKBY",
                       authors=[self.zed, self.amy], publisher=self.methuen)
        text = self.export(pub)
        self.assertIn("Zulu, Z., &amp; Alpha, A. (1960).", text)
        self.assertEqual(text.count("Zulu, Zed, and Amy Alpha. <i>Joint</i>"), 2)
        self.assertNotIn("et all", text)

    def test_many_authors_on_export_page(self):
        authors = [self.zed, self.amy] + [self.person(f"F{i}", f"L{i}")
                                          for i in range(3)]
        pub = self.pub("Big", 1960, pub_type="BKBY", authors=authors,
                       publisher=self.methuen)
        text = self.export(pub)
        self.assertEqual(text.count("et al."), 1)
        self.assertIn("Zulu, Zed, et al. <i>Big</i>", text)

    def edited_book(self, *editors):
        pub = self.pub("Lectures", 2006, pub_type="BKBY",
                       authors=[self.mo], publisher=self.methuen)
        pub.editors.add(*[self.person(f, l) for f, l in editors])
        text = self.export(pub)
        return (text[text.index("APA:"):text.index("MLA:")],
                text[text.index("MLA:"):text.index("Chicago:")],
                text[text.index("Chicago:"):])

    def test_single_editor(self):
        apa, mla, chicago = self.edited_book(("Timothy", "Fuller"))
        self.assertIn("(2006). <i>Lectures</i> (T. Fuller, Ed.). London,", apa)
        self.assertIn("<i>Lectures</i>. Edited by Timothy Fuller. London:", mla)
        self.assertIn("<i>Lectures</i>. Edited by Timothy Fuller. London:",
                      chicago)

    def test_two_editors(self):
        apa, mla, chicago = self.edited_book(("Terry", "Nardin"),
                                             ("Luke", "O'Sullivan"))
        self.assertIn("<i>Lectures</i> (T. Nardin &amp; L. O&#x27;Sullivan, Eds.).",
                      apa)
        for style in (mla, chicago):
            self.assertIn("Edited by Terry Nardin and Luke O&#x27;Sullivan.",
                          style)

    def test_no_editors(self):
        apa, mla, chicago = self.edited_book()
        self.assertIn("(2006). <i>Lectures</i>. London,", apa)
        self.assertNotIn("Edited by", mla + chicago)

    def test_no_authors(self):
        pub = self.pub("Anonymous", 1960, pub_type="BKBY", publisher=self.methuen)
        self.assertIn("(1960). <i>Anonymous</i>.", self.export(pub))

    def test_missing_publication_is_404(self):
        self.assertEqual(self.client.get("/oakeshott/export/999/").status_code, 404)
