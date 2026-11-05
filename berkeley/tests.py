from django.test import TestCase

from .models import Keyword, Person, Publication, Subject, UNKNOWN_ID


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
