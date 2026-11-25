"""Possible duplicates on the to-do page, and merging them."""
from berkeley.models import (Authorship, Candidate, IndexTerm, NotDuplicate,
                             Person, Publication)

from .test_todo import TODO_URL, TodoTestCase
from .helpers import ROOT


class DuplicatesTest(TodoTestCase):
    def setUp(self):
        super().setUp()
        self.login()
        self.parekh = self.person("Bhikhu", "Parekh", mname="C.")
        self.again = self.person("B.", "Parekh")
        self.other = self.person("Brian", "Parekh")
        self.chapter = self.pub("The Nature of Political Philosophy", 1968,
                                authors=[self.parekh],
                                collection=self.book, pages="153-208")
        self.twice = self.pub("The Nature of Political Philosophy", 1968,
                              authors=[self.again], collection=self.book)

    def merge(self, kind, keep, drop):
        return self.client.post(
            f"{ROOT}merge/{kind}/{keep.id}/{drop.id}/")

    def test_listed_on_the_todo_page(self):
        html = self.client.get(TODO_URL).content.decode()
        self.assertIn("Possible duplicates", html)
        self.assertIn(f"{ROOT}merge/person/{self.parekh.id}/"
                      f"{self.again.id}/", html)
        self.assertIn(f"{ROOT}merge/publication/{self.twice.id}/"
                      f"{self.chapter.id}/", html)
        # Brian is not Bhikhu (though either might be B.)
        self.assertNotIn(f"merge/person/{self.parekh.id}/{self.other.id}/",
                         html)
        self.assertIn(f"merge/person/{self.again.id}/{self.other.id}/",
                      html)

    def test_different_authors_are_different_entries(self):
        self.twice.authorship_set.all().delete()
        Authorship.objects.create(publication=self.twice, person=self.mo,
                                  position=1)
        html = self.client.get(TODO_URL).content.decode()
        self.assertNotIn(f"merge/publication/{self.twice.id}/", html)

    def test_merging_people(self):
        resp = self.merge("person", self.parekh, self.again)
        self.assertRedirects(resp, f"{TODO_URL}#duplicates",
                             fetch_redirect_response=False)
        self.assertFalse(Person.objects.filter(id=self.again.id).exists())
        self.assertEqual(self.twice.ordered_authors(), [self.parekh])

    def test_merging_entries_keeps_their_links(self):
        term = IndexTerm.objects.create(name="political philosophy")
        term.entries.add(self.twice)
        candidate = Candidate.objects.create(
            citation="x", status=Candidate.ADDED, entry=self.twice)
        self.twice.reprinted_in.add(self.chapter)
        self.merge("publication", self.chapter, self.twice)
        self.assertFalse(Publication.objects.filter(
            id=self.twice.id).exists())
        self.assertEqual(list(term.entries.all()), [self.chapter])
        candidate.refresh_from_db()
        self.assertEqual(candidate.entry, self.chapter)
        # not a reprint of itself; both authors, the kept one first
        self.assertFalse(self.chapter.reprinted_in.exists())
        self.assertEqual(self.chapter.ordered_authors(),
                         [self.parekh, self.again])

    def test_merging_a_book_keeps_its_chapters(self):
        book_again = self.pub(self.book.title, self.book.year)
        chapter = self.pub("A chapter", 1962, collection=book_again)
        self.merge("publication", self.book, book_again)
        chapter.refresh_from_db()
        self.assertEqual(chapter.collection, self.book)

    def test_a_shared_link_is_not_doubled(self):
        Authorship.objects.create(publication=self.chapter,
                                  person=self.again, position=2)
        self.merge("person", self.parekh, self.again)
        self.assertEqual(self.chapter.ordered_authors(), [self.parekh])

    def test_blank_fields_are_filled_from_the_other(self):
        self.merge("publication", self.twice, self.chapter)
        self.twice.refresh_from_db()
        self.assertEqual(self.twice.pages, "153-208")

    def test_not_the_same(self):
        self.client.post(f"{ROOT}not_duplicates/person/{self.again.id}/"
                         f"{self.parekh.id}/")
        self.assertTrue(NotDuplicate.objects.filter(
            kind="person", first_id=self.parekh.id,
            second_id=self.again.id).exists())
        html = self.client.get(TODO_URL).content.decode()
        self.assertNotIn(f"merge/person/{self.parekh.id}/", html)

    def test_get_does_not_merge(self):
        self.client.get(f"{ROOT}merge/person/{self.parekh.id}/"
                        f"{self.again.id}/")
        self.assertTrue(Person.objects.filter(id=self.again.id).exists())

    def test_editors_only(self):
        self.client.logout()
        self.merge("person", self.parekh, self.again)
        self.assertTrue(Person.objects.filter(id=self.again.id).exists())
