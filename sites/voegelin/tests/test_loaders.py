"""The Voegelin loaders, run on an empty test database."""
from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from berkeley.models import OpenQuestion, Publication

from sites.voegelin.management.commands._books_by import BOOKS, QUESTIONS


def load():
    out = StringIO()
    call_command("load_books_by_voegelin", stdout=out)
    return out.getvalue()


class BooksByVoegelinTest(TestCase):
    def setUp(self):
        self.first = load()

    def book(self, title):
        return Publication.objects.get(title=title)

    def test_every_book_once(self):
        self.assertEqual(Publication.objects.filter(pub_type="BKBY").count(),
                         len(BOOKS))
        self.assertIn(f"Added {len(BOOKS)} books", self.first)

    def test_rerun_adds_nothing(self):
        self.assertIn("Added 0 books", load())
        self.assertEqual(Publication.objects.count(), len(BOOKS))
        self.assertEqual(OpenQuestion.objects.count(), len(QUESTIONS))

    def test_keys_point_at_books(self):
        keys = {b["key"] for b in BOOKS}
        self.assertEqual(len(keys), len(BOOKS))
        for b in BOOKS:
            for key in [b.get("translation_of", "")] + b.get("reprints", []):
                self.assertTrue(not key or key in keys, (b["key"], key))
        for _, entries in QUESTIONS.values():
            self.assertLessEqual(set(entries), keys)

    def test_translation_and_reprint_links(self):
        original = self.book("Die politischen Religionen")
        english = self.book("Political Religions")
        self.assertEqual(original.language, "German")
        self.assertEqual(english.translation_of, original)
        self.assertEqual(
            [t.lname for t in english.translators.all().order_by("lname")],
            ["DiNapoli", "Easterly III"])
        oh1 = self.book("Order and History, Volume I: Israel and Revelation")
        self.assertEqual(
            [b.title for b in oh1.reprinted_in.all()],
            ["Order and History, Volume I: Israel and Revelation (The "
             "Collected Works of Eric Voegelin, Volume 14)"])

    def test_co_authors_in_order(self):
        letters = Publication.objects.get(title__startswith="Faith and "
                                          "Political Philosophy")
        self.assertEqual([p.lname for p in letters.ordered_authors()],
                         ["Strauss", "Voegelin"])
        self.assertEqual(
            [p.lname for p in self.book("Rasse und Staat").ordered_authors()],
            ["Voegelin"])
