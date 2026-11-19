"""The Voegelin loaders, run on an empty test database."""
from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from berkeley.models import Journal, OpenQuestion, Publication

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


class BooksAboutVoegelinTest(TestCase):
    def test_load_twice(self):
        from sites.voegelin.management.commands.load_books_about_voegelin \
            import BOOKS_ABOUT, MENTIONING
        out = StringIO()
        call_command("load_books_about_voegelin", stdout=out)
        self.assertIn(f"Added {len(BOOKS_ABOUT)} books about", out.getvalue())
        call_command("load_books_about_voegelin", stdout=out)
        self.assertEqual(Publication.objects.filter(pub_type="BKAB").count(),
                         len(BOOKS_ABOUT))
        self.assertEqual(Publication.objects.filter(pub_type="MENT").count(),
                         len(MENTIONING))
        recollected = Publication.objects.get(
            title="Voegelin Recollected: Conversations on a Life")
        self.assertEqual([p.lname for p in recollected.ordered_editors()],
                         ["Cooper", "Bruhn"])
        self.assertEqual(recollected.publisher.name,
                         "University of Missouri Press")
        self.assertEqual(recollected.subject.name, "Philosophy")


class KeywordsVoegelinTest(TestCase):
    def test_tags(self):
        load()
        out = StringIO()
        call_command("load_keywords_voegelin", stdout=out)
        call_command("load_keywords_voegelin", stdout=out)
        self.assertIn("Added 0 keyword tags.", out.getvalue())
        pub = Publication.objects.get(title="Die politischen Religionen")
        self.assertEqual([k.name for k in pub.keywords.all()],
                         ["political religions"])
        oh3 = Publication.objects.get(
            title="Order and History, Volume III: Plato and Aristotle")
        self.assertEqual(sorted(k.name for k in oh3.keywords.all()),
                         ["Aristotle", "Plato"])


class ShortWorksByVoegelinTest(TestCase):
    def test_load_twice(self):
        from sites.voegelin.management.commands import _short_works_by as d
        load()
        out = StringIO()
        call_command("load_short_works_by_voegelin", stdout=out)
        n = len(d.ARTICLES) + len(d.CHAPTERS)
        self.assertIn(f"Added {n} short works", out.getvalue())
        call_command("load_short_works_by_voegelin", stdout=out)
        self.assertIn("Added 0 short works", out.getvalue())
        self.assertEqual(Publication.objects.filter(pub_type="SWBY").count(),
                         n)
        self.assertEqual(Publication.objects.filter(pub_type="MENT").count(),
                         len(d.HOSTS))
        reprinted = [i for i in d.ARTICLES + d.CHAPTERS if i.get("reprinted")]
        self.assertEqual(
            Publication.objects.filter(pub_type="SWBY")
            .exclude(reprinted_in=None).distinct().count(), len(reprinted))
        timur = next(i for i in d.ARTICLES + d.CHAPTERS
                     if i["title"].startswith("Das Timurbild")
                     or "Timur" in i["title"])
        pub = Publication.objects.get(title=timur["title"])
        self.assertEqual(pub.language, timur["language"])
        self.assertEqual([p.lname for p in pub.ordered_authors()],
                         ["Voegelin"])


class ReviewsByVoegelinTest(TestCase):
    def test_load_twice(self):
        from sites.voegelin.management.commands import _reviews_by as d
        load()
        out = StringIO()
        call_command("load_reviews_by_voegelin", stdout=out)
        n = len(d.REVIEWS)
        self.assertIn(f"Added {n} reviews", out.getvalue())
        call_command("load_reviews_by_voegelin", stdout=out)
        self.assertIn("Added 0 reviews", out.getvalue())
        reviews = Publication.objects.filter(pub_type="RVBY")
        self.assertEqual(reviews.count(), n)
        self.assertEqual(
            reviews.exclude(reprinted_in=None).distinct().count(),
            len([r for r in d.REVIEWS if r.get("reprinted")]))
        self.assertEqual(OpenQuestion.objects.filter(
            title__startswith="Voegelin reviews").count(), len(d.QUESTIONS))
        first = d.REVIEWS[0]
        pub = reviews.get(review=first["book"], year=first["year"])
        self.assertEqual([p.lname for p in pub.ordered_authors()],
                         ["Voegelin"])
        self.assertEqual(pub.language, first["language"])
        self.assertEqual(
            sorted(p.lname for p in pub.reviewees.all()),
            sorted(n[2] for n in first["reviewees"]))

    def test_field_lengths(self):
        """Values fit their database columns (sqlite would not complain)."""
        from sites.voegelin.management.commands import _reviews_by as d
        for r in d.REVIEWS:
            for field in ("book", "names", "title", "journal", "volume",
                          "issue", "pages", "language"):
                model, column = {
                    "book": (Publication, "review"),
                    "names": (Publication, "reviewed_names"),
                    "journal": (Journal, "name"),
                }.get(field, (Publication, field))
                limit = model._meta.get_field(column).max_length
                self.assertLessEqual(len(r.get(field, "")), limit,
                                     (r["key"], field))
