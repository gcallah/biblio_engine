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
        self.assertIn(f"Added {total + len(data.REVIEWS)} short works",
                      self.load())
        self.assertIn("Added 0 short works", self.load())
        self.assertEqual(Publication.objects.filter(pub_type="SWAB").count(),
                         total)
        self.assertEqual(Publication.objects.filter(pub_type="RVAB").count(),
                         len(data.REVIEWS))
        self.assertEqual(Publication.objects.filter(pub_type="MENT").count(),
                         len(data.HOSTS))

    def test_oakeshott_in_every_title_except_the_listed_ones(self):
        from berkeley.management.commands import _short_works_about as data
        unnamed = {item["title"] for item in data.UNNAMED}
        self.load()
        for pub in Publication.objects.filter(pub_type="SWAB"):
            if pub.title not in unnamed:
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

    def test_editors_keep_title_page_order(self):
        self.load()
        host = Publication.objects.get(
            title="Conceptions of Liberty in Political Philosophy")
        self.assertEqual([e.lname for e in host.ordered_editors()],
                         ["Pelczynski", "Gray"])

    def test_needs_books_about_first(self):
        from django.core.management.base import CommandError
        Publication.objects.filter(pub_type="BKAB").delete()
        with self.assertRaises(CommandError):
            self.load()


class LoadAbstractsTest(TestCase):
    """Every abstract in _abstracts.py matches exactly one loaded entry."""

    def test_every_abstract_applies(self):
        from berkeley.management.commands._abstracts import ABSTRACTS
        for command in ("load_books_by_oakeshott",
                        "load_books_about_oakeshott",
                        "load_short_works_about_oakeshott",
                        "load_short_works_by_oakeshott"):
            call_command(command, stdout=StringIO())
        out = StringIO()
        call_command("load_abstracts", stdout=out)
        self.assertIn(f"Set {len(ABSTRACTS)} abstracts", out.getvalue())
        # Books by Oakeshott get theirs from book_info.py instead
        self.assertEqual(Publication.objects.exclude(abstract="").exclude(
            pub_type="BKBY").count(), len(ABSTRACTS))


class LoadAuthorInfoTest(TestCase):
    """Every entry in _author_info.py matches exactly one loaded person."""

    def test_every_entry_applies(self):
        from berkeley.management.commands._author_info import AUTHOR_INFO
        for command in ("load_books_by_oakeshott",
                        "load_books_about_oakeshott",
                        "load_short_works_about_oakeshott",
                        "load_short_works_by_oakeshott"):
            call_command(command, stdout=StringIO())
        out = StringIO()
        call_command("load_author_info", stdout=out)
        self.assertIn(f"Updated {len(AUTHOR_INFO)} people", out.getvalue())
        out = StringIO()
        call_command("load_author_info", stdout=out)
        self.assertIn("Updated 0 people", out.getvalue())


class LoadShortWorksByOakeshottTest(TestCase):
    def load(self, command="load_short_works_by_oakeshott"):
        out = StringIO()
        call_command(command, stdout=out)
        return out.getvalue()

    def test_loads_once_with_full_text_links(self):
        from berkeley.management.commands import _short_works_by as data
        self.load("load_books_by_oakeshott")
        total = len(data.ARTICLES) + len(data.CHAPTERS)
        self.assertIn(f"Added {total} short works", self.load())
        self.assertIn("Added 0 short works", self.load())
        works = Publication.objects.filter(pub_type="SWBY")
        self.assertEqual(works.count(), total)
        linked = {i["title"] for i in data.ARTICLES + data.CHAPTERS
                  if i.get("url")}
        for pub in works:
            if pub.title in linked:
                self.assertTrue(pub.url.startswith("https://"), pub.title)
            else:
                self.assertEqual(pub.url, "", pub.title)
            self.assertEqual(pub.ordered_authors()[0].lname, "Oakeshott")
        moral = works.get(title__startswith="The Moral Life")
        self.assertEqual(moral.collection.pub_type, "BKBY")
        self.assertEqual(moral.year, 1962)


class LoadReviewsByOakeshottTest(TestCase):
    def load(self):
        out = StringIO()
        call_command("load_reviews_by_oakeshott", stdout=out)
        return out.getvalue()

    def setUp(self):
        call_command("load_books_by_oakeshott", stdout=StringIO())

    def test_loads_every_review_once(self):
        from berkeley.management.commands import _reviews_by as data
        total = len(data.REVIEWS)
        self.assertGreater(total, 150)
        self.assertIn(f"Added {total} reviews", self.load())
        self.assertIn("Added 0 reviews", self.load())
        self.assertIn("updated 0", self.load())
        reviews = Publication.objects.filter(pub_type="RVBY")
        self.assertEqual(reviews.count(), total)
        for pub in reviews:
            self.assertEqual(pub.ordered_authors()[0].lname, "Oakeshott")
            self.assertTrue(pub.review and pub.reviewed_names, pub.id)
            self.assertTrue(pub.reviewees.exists(), pub.review)

    def test_reuses_people_by_last_name_and_initial(self):
        from berkeley.models import Person
        Person.objects.create(fname="Maurice", lname="Cranston")
        self.load()
        self.assertEqual(Person.objects.filter(lname="Cranston").count(), 1)
        self.assertTrue(Publication.objects.filter(
            pub_type="RVBY", reviewees__fname="Maurice").exists())

    def test_reprints_link_to_the_collected_volumes(self):
        from berkeley.management.commands import _reviews_by as data
        self.load()
        cpj = Publication.objects.get(title=data.CPJ, pub_type="BKBY")
        vmes = Publication.objects.get(title=data.VMES, pub_type="BKBY")
        self.assertGreater(cpj.reprints.count(), 100)
        self.assertGreater(vmes.reprints.count(), 50)
        self.assertFalse(cpj.reprints.filter(year__gt=1951).exists())
        self.assertFalse(vmes.reprints.filter(year__lt=1952).exists())
        carr = Publication.objects.get(title__startswith="Mr. Carr")
        self.assertEqual(list(carr.reprinted_in.all()), [cpj])
        collingwood = Publication.objects.get(review="The Principles of Art")
        self.assertEqual(
            sorted(b.pub_type for b in collingwood.reprinted_in.all()),
            ["BKBY", "MENT"])
        self.assertIn("updated 0", self.load())

    def test_needs_books_by_first(self):
        from django.core.management.base import CommandError
        Publication.objects.all().delete()
        with self.assertRaises(CommandError):
            self.load()
