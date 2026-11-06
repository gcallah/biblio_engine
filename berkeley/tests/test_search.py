"""The /publications/ search: each filter on its own and in combination."""
import re
from berkeley.models import Keyword, Subject

from .helpers import PUBS_URL, BiblioTestCase


class KeywordSearchTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.kw = Keyword.objects.create(name="liberty")
        self.tagged = self.pub("Tagged", 1950)
        self.tagged.keywords.add(self.kw)
        self.untagged = self.pub("Untagged", 1951)

    def test_keyword_filter_applied(self):
        self.assertEqual(self.results(keyword1=self.kw.id), [self.tagged])

    def test_blank_search_returns_everything(self):
        self.assertEqual(self.results(), [self.tagged, self.untagged])

    def test_no_params_at_all_returns_everything(self):
        resp = self.client.get(PUBS_URL)
        self.assertEqual(list(resp.context["pub_list"]),
                         [self.tagged, self.untagged])


class AuthorSearchTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        mo = self.person("Michael", "Oakeshott")
        berlin = self.person("Isaiah", "Berlin")
        self.coauthored = self.pub("Both", 1950, authors=[mo, berlin])
        self.solo = self.pub("Solo", 1951, authors=[berlin])

    def test_partial_case_insensitive_match(self):
        self.assertEqual(self.results(lname="oakes"), [self.coauthored])
        self.assertEqual(self.results(lname="OAKESHOTT"), [self.coauthored])

    def test_matches_middle_of_name(self):
        self.assertEqual(self.results(lname="erl"), [self.coauthored, self.solo])

    def test_no_duplicates_when_several_authors_match(self):
        # "e" matches both Oakeshott and Berlin on the co-authored piece.
        self.assertEqual(self.results(lname=" e "), [self.coauthored, self.solo])

    def test_whitespace_only_is_ignored(self):
        self.assertEqual(self.results(lname="   "), [self.coauthored, self.solo])

    def test_no_match(self):
        self.assertEqual(self.results(lname="hobbes"), [])


class TypeSearchTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.book = self.pub("Rationalism in Politics", 1962, pub_type="BKBY")
        self.about = self.pub("A study of Oakeshott", 1990, pub_type="SWAB")

    def test_type_filter(self):
        self.assertEqual(self.results(pub_type="BKBY"), [self.book])
        self.assertEqual(self.results(pub_type="SWAB"), [self.about])

    def test_type_with_no_entries(self):
        self.assertEqual(self.results(pub_type="MENT"), [])

    def test_unknown_type_finds_nothing(self):
        self.assertEqual(self.results(pub_type="ZZZZ"), [])


class ReviewTypeSearchTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.book = self.pub("The Politics of Faith", 1996, pub_type="BKBY")
        self.review = self.pub("", 1997, pub_type="RVAB",
                               pub_reviewed=self.book)
        self.by_mo = self.pub("Review by MO", 1950, pub_type="RVBY")

    def test_filter_by_review_type(self):
        self.assertEqual(self.results(pub_type="RVAB"), [self.review])
        self.assertEqual(self.results(pub_type="RVBY"), [self.by_mo])

    def test_untitled_review_listed_by_reviewed_book(self):
        self.assertContains(self.search(pub_type="RVAB"),
                            "A Review of The Politics of Faith")


class YearRangeSearchTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.p1933 = self.pub("Experience", 1933)
        self.p1962 = self.pub("Rationalism", 1962)
        self.p1975 = self.pub("Human Conduct", 1975)
        self.all = [self.p1933, self.p1962, self.p1975]

    def test_both_blank_returns_everything(self):
        self.assertEqual(self.results(), self.all)

    def test_range_is_inclusive(self):
        self.assertEqual(self.results(start_year="1933", end_year="1962"),
                         [self.p1933, self.p1962])

    def test_single_year(self):
        self.assertEqual(self.results(start_year="1962", end_year="1962"),
                         [self.p1962])

    def test_blank_start_finds_up_to_end(self):
        self.assertEqual(self.results(end_year="1962"), [self.p1933, self.p1962])

    def test_blank_end_finds_from_start(self):
        self.assertEqual(self.results(start_year="1962"), [self.p1962, self.p1975])

    def test_start_after_end_finds_nothing(self):
        self.assertEqual(self.results(start_year="1970", end_year="1940"), [])

    def test_non_numeric_year_is_ignored(self):
        self.assertEqual(self.results(start_year="abc"), self.all)
        self.assertEqual(self.results(end_year="19x0"), self.all)
        self.assertEqual(self.results(start_year="-5"), self.all)

    def test_padded_year_is_accepted(self):
        self.assertEqual(self.results(start_year=" 1975 "), [self.p1975])


class SubjectSearchTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.politics = Subject.objects.create(name="Politics")
        self.in_politics = self.pub("A", 1950, subject=self.politics)
        self.unfiled = self.pub("B", 1951)

    def test_subject_filter(self):
        self.assertEqual(self.results(subject=self.politics.id),
                         [self.in_politics])


class CombinedSearchTest(BiblioTestCase):
    """Filters are ANDed together."""

    def setUp(self):
        super().setUp()
        mo = self.person("Michael", "Oakeshott")
        other = self.person("Isaiah", "Berlin")
        self.kw = Keyword.objects.create(name="history")
        self.match = self.pub("Match", 1962, authors=[mo], pub_type="BKBY")
        self.match.keywords.add(self.kw)
        self.wrong_type = self.pub("Wrong type", 1962, authors=[mo],
                                   pub_type="SWBY")
        self.wrong_type.keywords.add(self.kw)
        self.wrong_year = self.pub("Wrong year", 1990, authors=[mo],
                                   pub_type="BKBY")
        self.wrong_year.keywords.add(self.kw)
        self.wrong_author = self.pub("Wrong author", 1962, authors=[other],
                                     pub_type="BKBY")
        self.wrong_author.keywords.add(self.kw)
        self.no_keyword = self.pub("No keyword", 1962, authors=[mo],
                                   pub_type="BKBY")

    def test_all_filters_together(self):
        self.assertEqual(
            self.results(lname="oake", pub_type="BKBY", start_year="1950",
                         end_year="1970", keyword1=self.kw.id),
            [self.match])

    def test_author_and_keyword_do_not_duplicate(self):
        two_authors = self.pub("Two", 1963,
                               authors=[self.person("Ann", "Oaks"),
                                        self.person("Bob", "Oakley")])
        two_authors.keywords.add(self.kw)
        found = self.results(lname="oak", keyword1=self.kw.id)
        self.assertEqual(found.count(two_authors), 1)


class ResultsPageTest(BiblioTestCase):
    def test_results_sorted_by_year(self):
        late = self.pub("Late", 1980)
        early = self.pub("Early", 1930)
        middle = self.pub("Middle", 1950)
        self.assertEqual(self.results(), [early, middle, late])

    def test_no_results_page(self):
        resp = self.search(lname="nobody")
        self.assertContains(resp, "No publications found")
        self.assertContains(resp, 'href="/oakeshott/"')
        self.assertNotContains(resp, "<caption>")

    def test_results_table_links(self):
        author = self.person("Michael", "Oakeshott")
        pub = self.pub("Experience and its Modes", 1933, authors=[author])
        resp = self.search()
        self.assertContains(resp, f'href="/oakeshott/pub_detail/{pub.id}/"')
        self.assertContains(resp, f'href="/oakeshott/export/{pub.id}/"')
        self.assertContains(resp, f'href="/oakeshott/person_detail/{author.id}/"')

    def test_long_journal_names_shown_whole_and_clamped(self):
        from berkeley.models import Journal
        name = "Conference for the Study of Political Thought Newsletter"
        self.pub("A Note", 1991, journal=Journal.objects.create(name=name))
        resp = self.search()
        self.assertContains(
            resp, f'<span class="clamp3" title="{name}">{name}</span>')

    def test_editors_shown_in_author_column(self):
        mo = self.person("Michael", "Oakeshott")
        collected = self.pub("The Voice of Liberal Learning", 1989,
                             authors=[mo])
        collected.editors.add(self.person("Timothy", "Fuller"))
        edited = self.pub("A Companion", 2012)
        edited.editors.add(self.person("Paul", "Franco"),
                           self.person("Leslie", "Marsh"))
        text = re.sub(r"<[^>]+>", "", re.sub(r"\s+", " ",
                                             self.search().content.decode()))
        self.assertIn("Oakeshott; Fuller (ed.)", text)
        self.assertIn("Franco, Marsh (eds.)", text)

    def test_abstract_column_links_and_pops_up_only_with_an_abstract(self):
        with_abs = self.pub("Rationalism", 1962, abstract="Essays on politics.")
        self.pub("No Abstract", 1963)
        html = re.sub(r"\s+", " ", self.search().content.decode())
        self.assertIn("<th>Abstract</th>", html)
        self.assertEqual(html.count('<td class="has-abstract">'), 1)
        self.assertIn(f'<td class="has-abstract"> <a href="/oakeshott/'
                      f'pub_detail/{with_abs.id}/">Abstract</a>', html)
        self.assertIn("Essays on politics.", html)
        # the record without an abstract gets an empty cell
        row = html[html.index("No Abstract"):]
        row = row[:row.index("</tr>")]
        self.assertIn("<td></td>", row)
        # the title cell no longer carries the popup
        title_cell = html[html.index("<td> <a href"):]
        self.assertNotIn("abstract-pop",
                         title_cell[:title_cell.index("</td>")])

    def test_full_text_link_only_when_there_is_a_url(self):
        self.pub("Work and Play", 1995, url="https://example.org/work")
        self.pub("Offline", 1996)
        resp = self.search()
        self.assertContains(
            resp, '<a class="fulltext" href="https://example.org/work">', 1)

    def test_long_titles_shown_whole_and_clamped_to_three_lines(self):
        """The full title is sent; CSS (.clamp3) limits it to three
        lines, and the title attribute shows it all on hover."""
        self.pub("x" * 80, 1950)
        resp = self.search()
        self.assertContains(
            resp, f'<span class="clamp3" title="{"x" * 80}">{"x" * 80}</span>')

    def test_results_list_authors_in_title_page_order(self):
        zed, amy = self.person("Zed", "Zulu"), self.person("Amy", "Alpha")
        self.pub("Joint", 1960, authors=[zed, amy])
        html = self.search().content.decode()
        self.assertLess(html.index("Zulu"), html.index("Alpha"))
