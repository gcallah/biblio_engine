import re

from django.test import TestCase

from .models import Journal, Keyword, Person, Publication, Subject, UNKNOWN_ID


class KeywordSearchTest(TestCase):
    def setUp(self):
        Subject.objects.create(id=UNKNOWN_ID, name="Unknown")
        self.kw = Keyword.objects.create(name="liberty")
        self.tagged = Publication.objects.create(title="Tagged", year=1950)
        self.tagged.keywords.add(self.kw)
        self.untagged = Publication.objects.create(title="Untagged", year=1951)

    def search(self, **params):
        query = {"lname": "", "pub_type": "", "subject": "", "keyword1": ""}
        query.update(params)
        resp = self.client.get("/oakeshott/publications/", query)
        return list(resp.context["pub_list"])

    def test_keyword_filter_applied(self):
        self.assertEqual(self.search(keyword1=self.kw.id), [self.tagged])

    def test_blank_search_returns_everything(self):
        self.assertEqual(self.search(), [self.tagged, self.untagged])


class AuthorSearchTest(TestCase):
    def setUp(self):
        Subject.objects.create(id=UNKNOWN_ID, name="Unknown")
        mo = Person.objects.create(fname="Michael", lname="Oakeshott")
        other = Person.objects.create(fname="Isaiah", lname="Berlin")
        self.coauthored = Publication.objects.create(title="Both", year=1950)
        self.coauthored.authors.add(mo, other)
        self.solo = Publication.objects.create(title="Solo", year=1951)
        self.solo.authors.add(other)

    def search(self, lname):
        query = {"lname": lname, "pub_type": "", "subject": "", "keyword1": ""}
        resp = self.client.get("/oakeshott/publications/", query)
        return list(resp.context["pub_list"])

    def test_partial_case_insensitive_match(self):
        self.assertEqual(self.search("oakes"), [self.coauthored])

    def test_no_duplicates_when_several_authors_match(self):
        # "e" matches both Oakeshott and Berlin on the co-authored piece.
        self.assertEqual(self.search(" e "), [self.coauthored, self.solo])


class TypeSearchTest(TestCase):
    def setUp(self):
        Subject.objects.create(id=UNKNOWN_ID, name="Unknown")
        self.book = Publication.objects.create(
            title="Rationalism in Politics", year=1962, pub_type="BKBY")
        self.about = Publication.objects.create(
            title="A study of Oakeshott", year=1990, pub_type="SWAB")

    def test_type_filter(self):
        query = {"lname": "", "pub_type": "BKBY", "subject": "", "keyword1": ""}
        resp = self.client.get("/oakeshott/publications/", query)
        self.assertEqual(list(resp.context["pub_list"]), [self.book])

    def test_search_form_offers_new_types(self):
        resp = self.client.get("/oakeshott/")
        for label in ("Books by Oakeshott", "Short Works by Oakeshott",
                      "Books About Oakeshott", "Short Works About Oakeshott",
                      "Works Mentioning Oakeshott",
                      "Book Reviews by Oakeshott",
                      "Book Reviews of Books About Oakeshott"):
            self.assertContains(resp, label)

    def test_export_uses_book_format(self):
        resp = self.client.get(f"/oakeshott/export/{self.book.id}/")
        self.assertEqual(resp.status_code, 200)


class YearRangeSearchTest(TestCase):
    def setUp(self):
        Subject.objects.create(id=UNKNOWN_ID, name="Unknown")
        self.p1933 = Publication.objects.create(title="Experience", year=1933)
        self.p1962 = Publication.objects.create(title="Rationalism", year=1962)
        self.p1975 = Publication.objects.create(title="Human Conduct", year=1975)

    def search(self, start="", end=""):
        query = {"lname": "", "pub_type": "", "start_year": start,
                 "end_year": end, "subject": "", "keyword1": ""}
        resp = self.client.get("/oakeshott/publications/", query)
        return list(resp.context["pub_list"])

    def test_both_blank_returns_everything(self):
        self.assertEqual(self.search(), [self.p1933, self.p1962, self.p1975])

    def test_range_is_inclusive(self):
        self.assertEqual(self.search("1933", "1962"), [self.p1933, self.p1962])

    def test_blank_start_finds_up_to_end(self):
        self.assertEqual(self.search(end="1962"), [self.p1933, self.p1962])

    def test_blank_end_finds_from_start(self):
        self.assertEqual(self.search(start="1962"), [self.p1962, self.p1975])

    def test_non_numeric_year_is_ignored(self):
        self.assertEqual(self.search(start="abc"), [self.p1933, self.p1962, self.p1975])

    def test_form_shows_year_fields(self):
        resp = self.client.get("/oakeshott/")
        self.assertContains(resp, 'name="start_year"')
        self.assertContains(resp, 'name="end_year"')


class ReviewTypeTest(TestCase):
    def setUp(self):
        Subject.objects.create(id=UNKNOWN_ID, name="Unknown")
        self.book = Publication.objects.create(
            title="The Politics of Faith", year=1996, pub_type="BKBY")
        self.review = Publication.objects.create(
            year=1997, pub_type="RVAB", pub_reviewed=self.book)
        self.by_mo = Publication.objects.create(
            title="Review by MO", year=1950, pub_type="RVBY")

    def search(self, pub_type):
        query = {"lname": "", "pub_type": pub_type, "subject": "", "keyword1": ""}
        return self.client.get("/oakeshott/publications/", query)

    def test_filter_by_review_type(self):
        resp = self.search("RVAB")
        self.assertEqual(list(resp.context["pub_list"]), [self.review])
        self.assertEqual(list(self.search("RVBY").context["pub_list"]), [self.by_mo])

    def test_untitled_review_shows_reviewed_book(self):
        self.assertEqual(str(self.review), "A Review of The Politics of Faith")
        self.assertContains(self.search("RVAB"), "A Review of The Politics of Faith")

    def test_review_export_renders(self):
        resp = self.client.get(f"/oakeshott/export/{self.review.id}/")
        self.assertEqual(resp.status_code, 200)


class ReviewCitationTest(TestCase):
    def setUp(self):
        Subject.objects.create(id=UNKNOWN_ID, name="Unknown")
        mo = Person.objects.create(fname="Michael", lname="Oakeshott")
        reviewer = Person.objects.create(fname="Jane", lname="Critic")
        self.book = Publication.objects.create(
            title="On Human Conduct", year=1975, pub_type="BKBY")
        self.book.authors.add(mo)
        journal = Journal.objects.create(name="Political Theory")
        self.review = Publication.objects.create(
            title="Conduct Considered", year=1976, pub_type="RVAB",
            pub_reviewed=self.book, journal=journal, volume="4",
            issue="2", month="May", pages="1-9")
        self.review.authors.add(reviewer)

    def export_text(self, pub):
        html = self.client.get(f"/oakeshott/export/{pub.id}/").content.decode()
        return re.sub(r"\s+", " ", html)

    def test_reviewed_authors(self):
        self.assertEqual(self.review.reviewed_authors(), "Michael Oakeshott")
        self.book.authors.add(Person.objects.create(fname="A", lname="B"),
                              Person.objects.create(fname="C", lname="D"))
        self.assertEqual(self.review.reviewed_authors(),
                         "A B, C D and Michael Oakeshott")  # ordered by last name

    def test_apa(self):
        self.assertIn("(1976). Conduct Considered [Review of the book "
                      "<i>On Human Conduct</i>, by Michael Oakeshott].",
                      self.export_text(self.review))

    def test_mla_and_chicago(self):
        text = self.export_text(self.review)
        phrase = ('"Conduct Considered." Review of <i>On Human Conduct</i>, '
                  'by Michael Oakeshott. <i>Political Theory</i>')
        self.assertEqual(text.count(phrase), 2)
        self.assertIn("<i>Political Theory</i> 4, no. 2 (1976): 1-9.", text)

    def test_untitled_review_without_reviewed_book(self):
        self.review.title = ""
        self.review.pub_reviewed = None
        self.review.save()
        text = self.export_text(self.review)
        self.assertNotIn("Review of", text)
        self.assertNotIn('""', text)
