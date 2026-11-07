"""The /export/<id>/ page: APA, MLA and Chicago citations for each type."""
from berkeley.models import Address, Journal, Publisher

from .helpers import PUBS_URL, BiblioTestCase, squash


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

    def test_title_ending_in_full_stop_gets_no_second_one(self):
        book = self.pub("Montaigne, Hegel, et al.", 2000, pub_type="BKAB",
                        publisher=self.methuen)
        text = self.export(book)
        self.assertNotIn("et al.</i>.", text)
        self.assertEqual(text.count("<i>Montaigne, Hegel, et al.</i>"), 3)

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


class CitationSnippetTest(CitationTestCase):
    """/export/<id>/citations/ - the rows the results-table popup loads."""

    def test_snippet_has_citations_but_no_page_layout(self):
        book = self.pub("Rationalism in Politics", 1962, pub_type="BKBY",
                        authors=[self.mo], publisher=self.methuen)
        resp = self.client.get(f"/oakeshott/export/{book.id}/citations/")
        self.assertEqual(resp.status_code, 200)
        html = resp.content.decode()
        self.assertIn('<table class="cite-table">', html)
        for style in ("APA:", "MLA:", "Chicago:"):
            self.assertIn(style, html)
        self.assertIn("Oakeshott, M. (1962).", " ".join(html.split()))
        self.assertNotIn("<html", html)
        self.assertNotIn("{#", html)
        self.assertNotIn("comment", html)

    def test_missing_publication_is_404(self):
        self.assertEqual(
            self.client.get("/oakeshott/export/9999/citations/").status_code,
            404)


class ChapterCitationTest(CitationTestCase):
    def setUp(self):
        super().setUp()
        self.book = self.pub("The Legacy", 2005, pub_type="BKAB",
                             publisher=self.methuen)
        self.book.editors.add(self.person("Corey", "Abel"),
                              self.person("Timothy", "Fuller"))
        self.chapter = self.pub("Spinoza and Oakeshott", 2005,
                                pub_type="SWAB", authors=[self.critic],
                                collection=self.book, pages="62-85")

    def test_apa(self):
        self.assertIn("Critic, J. (2005). Spinoza and Oakeshott. In C. Abel "
                      "&amp; T. Fuller (Eds.), <i>The Legacy</i> (pp. 62-85). "
                      "London, England: Methuen.", self.export(self.chapter))

    def test_mla(self):
        self.assertIn('"Spinoza and Oakeshott." <i>The Legacy</i>, edited by '
                      'Corey Abel and Timothy Fuller, Methuen, 2005, '
                      'pp. 62-85.', self.export(self.chapter))

    def test_chicago(self):
        self.assertIn('"Spinoza and Oakeshott." In <i>The Legacy</i>, edited '
                      'by Corey Abel and Timothy Fuller, 62-85. London: '
                      'Methuen, 2005.', self.export(self.chapter))

    def test_single_page_and_question_mark(self):
        self.chapter.title = "Why Read Oakeshott?"
        self.chapter.pages = "562"
        self.chapter.save()
        text = self.export(self.chapter)
        self.assertIn("Why Read Oakeshott? In", text)
        self.assertIn("(p. 562)", text)

    def test_detail_page_links_to_book(self):
        text = self.page_text(f"/oakeshott/pub_detail/{self.chapter.id}/")
        self.assertIn(f'href="/oakeshott/pub_detail/{self.book.id}/"', text)


class JournalDateCitationTest(CitationTestCase):
    def test_newspaper_day_and_no_issue(self):
        pub = self.pub("Michael Oakeshott, RIP", 1991, pub_type="SWAB",
                       journal=self.journal, volume="43", month="January",
                       day="28", pages="19-20")
        text = self.export(pub)
        self.assertIn("(1991, January 28). Michael Oakeshott, RIP.", text)
        self.assertIn("<i>Political Theory</i>, 43 (January 28, 1991): 19-20.",
                      text)


    def test_newspaper_without_volume_or_pages(self):
        pub = self.pub("Arguing with Oakeshott", 2003, pub_type="SWAB",
                       journal=self.journal, month="December", day="27")
        text = self.export(pub)
        self.assertIn("Arguing with Oakeshott. <i>Political Theory</i>.", text)
        self.assertIn("<i>Political Theory</i> 27 December 2003.", text)
        self.assertIn("<i>Political Theory</i> (December 27, 2003).", text)


class MentioningCitationTest(CitationTestCase):
    def test_book_without_journal_uses_book_format(self):
        pub = self.pub("Cambridge Minds", 1994, pub_type="MENT",
                       publisher=self.methuen)
        self.assertIn("(1994). <i>Cambridge Minds</i>. London, England: "
                      "Methuen.", self.export(pub))

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
        self.assertIn("<i>Political Theory</i> 4, no. 2 (May 1976): 1-9.", text)

    def test_reviews_by_oakeshott_use_review_format(self):
        self.review.pub_type = "RVBY"
        self.review.save()
        self.assertIn("[Review of the book", self.export(self.review))

    def test_reviews_of_books_by_oakeshott_use_review_format(self):
        self.review.pub_type = "RVOB"
        self.review.save()
        text = self.export(self.review)
        self.assertIn("[Review of the book", text)
        self.assertIn("Review of <i>On Human Conduct</i>", text)

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


class ReviewOfBookNotInBibliographyTest(CitationTestCase):
    """Oakeshott's reviews: the reviewed book is only a title and names."""
    def setUp(self):
        super().setUp()
        self.tls = Journal.objects.create(name="Times Literary Supplement")

    def review(self, **kw):
        fields = dict(pub_type="RVBY", authors=[self.mo],
                      review="Science, Religion and Reality",
                      reviewed_names="J. Needham (ed.)",
                      journal=self.journal, volume="27", pages="317-319")
        fields.update(kw)
        return self.pub(fields.pop("title", ""), 1926, **fields)

    def test_every_style(self):
        text = self.export(self.review())
        self.assertIn("Oakeshott, M. (1926). [Review of the book "
                      "<i>Science, Religion and Reality</i>, by J. Needham "
                      "(ed.)]. <i>Political Theory, 27</i>, 317-319.", text)
        self.assertEqual(text.count(
            "Review of <i>Science, Religion and Reality</i>, by J. Needham "
            "(ed.). <i>Political Theory</i>"), 2)
        self.assertIn("<i>Political Theory</i> 27 (1926): 317-319.", text)

    def test_newspaper_date_without_volume(self):
        text = self.export(self.review(journal=self.tls, volume="",
                                       day="15", month="January", pages="45"))
        self.assertIn("(1926, January 15).", text)
        self.assertIn("<i>Times Literary Supplement</i>, 45.", text)
        self.assertIn("(January 15, 1926): 45.", text)
        self.assertNotIn(", ,", text)

    def test_names_ending_in_full_stop(self):
        text = self.export(self.review(reviewed_names="T.A. Spragens, Jr.",
                                       title="Logos and Telos"))
        self.assertNotIn("Jr..", text)
        self.assertIn('"Logos and Telos." Review of', text)

    def test_listing_shows_reviewed_book(self):
        self.review(title="Logos and Telos")
        self.review()
        text = squash(self.client.get(PUBS_URL, {"pub_type": "RVBY"})
                      .content.decode())
        self.assertIn("Review of J. Needham (ed.), Science, Religion and "
                      "Reality", text)
        self.assertIn("Logos and Telos [Review of J. Needham (ed.), "
                      "Science, Religion and Reality]", text)


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

    def test_editors_in_title_page_order_not_alphabetical(self):
        from berkeley.models import Editorship
        pub = self.pub("Tradition", 2018, pub_type="BKAB",
                       publisher=self.methuen)
        callahan = self.person("Gene", "Callahan")
        trepanier = self.person("Lee", "Trepanier")
        # created out of order on purpose; position decides
        Editorship.objects.create(publication=pub, person=callahan,
                                  position=2)
        Editorship.objects.create(publication=pub, person=trepanier,
                                  position=1)
        text = self.export(pub)
        self.assertIn("(L. Trepanier &amp; G. Callahan, Eds.)", text)
        self.assertIn("Edited by Lee Trepanier and Gene Callahan.", text)
        page = self.page_text("/oakeshott/publications/?pub_type=BKAB")
        self.assertRegex(page, r"Trepanier</a>, <a[^>]*>Callahan</a> \(eds\.\)")

    def test_no_editors(self):
        apa, mla, chicago = self.edited_book()
        self.assertIn("(2006). <i>Lectures</i>. London,", apa)
        self.assertNotIn("Edited by", mla + chicago)

    def test_no_authors(self):
        pub = self.pub("Anonymous", 1960, pub_type="BKBY", publisher=self.methuen)
        self.assertIn("(1960). <i>Anonymous</i>.", self.export(pub))

    def test_missing_publication_is_404(self):
        self.assertEqual(self.client.get("/oakeshott/export/999/").status_code, 404)
