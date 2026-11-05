from django.test import TestCase

from .models import Keyword, Publication, Subject, UNKNOWN_ID


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
