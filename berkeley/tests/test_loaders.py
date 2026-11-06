"""Data-loading management commands."""
from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from berkeley.management.commands.load_books_by_oakeshott import BOOKS
from berkeley.models import Publication, Publisher


class LoadBooksByOakeshottTest(TestCase):
    def load(self):
        out = StringIO()
        call_command("load_books_by_oakeshott", stdout=out)
        return out.getvalue()

    def test_loads_every_book_once(self):
        self.assertIn(f"Added {len(BOOKS)} books", self.load())
        self.assertIn("Added 0 books", self.load())
        self.assertEqual(Publication.objects.filter(pub_type="BKBY").count(),
                         len(BOOKS))

    def test_titles_are_unique(self):
        titles = [b["title"] for b in BOOKS]
        self.assertEqual(len(titles), len(set(titles)))

    def test_oakeshott_is_first_author(self):
        self.load()
        for pub in Publication.objects.all():
            self.assertEqual(pub.ordered_authors()[0].lname, "Oakeshott",
                             pub.title)

    def test_coauthor_order(self):
        self.load()
        guide = Publication.objects.get(title__startswith="A Guide")
        self.assertEqual([a.lname for a in guide.ordered_authors()],
                         ["Oakeshott", "Griffith"])

    def test_same_press_in_two_cities(self):
        self.load()
        cities = {p.publisher.address.city for p in Publication.objects.filter(
            publisher__name="Bowes & Bowes")}
        self.assertEqual(cities, {"Cambridge", "London"})
        self.assertEqual(Publisher.objects.filter(name="Bowes & Bowes").count(), 2)

    def test_every_page_renders(self):
        self.load()
        for pub in Publication.objects.all():
            for route in ("pub_detail", "export"):
                resp = self.client.get(f"/oakeshott/{route}/{pub.id}/")
                self.assertEqual(resp.status_code, 200, (route, pub.title))
        resp = self.client.get("/oakeshott/publications/", {"pub_type": "BKBY"})
        self.assertEqual(len(resp.context["pub_list"]), len(BOOKS))

    def test_both_editions_of_rationalism(self):
        self.load()
        years = sorted(Publication.objects.filter(
            title__startswith="Rationalism in Politics").values_list("year", flat=True))
        self.assertEqual(years, [1962, 1991])


class LoadShortWorksAboutOakeshottTest(TestCase):
    """load_short_works_about_oakeshott, on top of the Books About."""

    def load(self, command="load_short_works_about_oakeshott"):
        out = StringIO()
        call_command(command, stdout=out)
        return out.getvalue()

    def setUp(self):
        self.load("load_books_about_oakeshott")

    def test_loads_every_short_work_once(self):
        from berkeley.management.commands import _short_works_about as data
        total = len(data.ARTICLES) + len(data.CHAPTERS)
        self.assertIn(f"Added {total} short works", self.load())
        self.assertIn("Added 0 short works", self.load())
        self.assertEqual(Publication.objects.filter(pub_type="SWAB").count(),
                         total)
        self.assertEqual(Publication.objects.filter(pub_type="MENT").count(),
                         len(data.HOSTS))

    def test_oakeshott_in_every_title(self):
        self.load()
        for pub in Publication.objects.filter(pub_type="SWAB"):
            self.assertIn("oakeshott", pub.title.lower(), pub.title)

    def test_chapters_link_to_existing_books_about(self):
        self.load()
        chapter = Publication.objects.get(title="Spinoza and Oakeshott")
        self.assertEqual(chapter.collection.pub_type, "BKAB")
        self.assertEqual(chapter.year, 2005)
        self.assertEqual(Publication.objects.filter(
            title="The Intellectual Legacy of Michael Oakeshott").count(), 1)

    def test_same_title_in_different_places_kept_apart(self):
        self.load()
        self.assertEqual(Publication.objects.filter(
            title="The Work of Michael Oakeshott").count(), 2)

    def test_needs_books_about_first(self):
        from django.core.management.base import CommandError
        Publication.objects.filter(pub_type="BKAB").delete()
        with self.assertRaises(CommandError):
            self.load()
