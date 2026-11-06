"""Load the "Short Works About Oakeshott" entries into the database.

A short work counts as being about Oakeshott if his name is in its
title. The data, and where it comes from, is in _short_works_about.py.

Journal articles are linked to a Journal. Chapters are linked
(Publication.collection) to their book. If the book is a Books About
Oakeshott entry it must already be in the database (run
load_books_about_oakeshott first); any other book is stored as a
"Works Mentioning Oakeshott" entry.

Safe to re-run: people, publishers, journals and books are matched on
their names, and short works on title, year and journal or book, so
running it twice does not create duplicates. Subjects are applied to
every short work, new or existing, so re-running picks up edits to them.

    python manage.py load_short_works_about_oakeshott
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import (
    Authorship, Journal, Publication, Subject, UNKNOWN_ID,
)

from . import _short_works_about as data
from ._loaders import get_person, get_publisher


def add_people(pub, item):
    for pos, name in enumerate(item.get("authors", []), 1):
        Authorship.objects.create(publication=pub, person=get_person(name),
                                  position=pos)
    for name in item.get("editors", []):
        pub.editors.add(get_person(name))


def get_host(key):
    """The book a chapter is in: an existing Books About Oakeshott entry
    (key is its title) or a HOSTS entry, stored as Works Mentioning."""
    if key not in data.HOSTS:
        try:
            return Publication.objects.get(title=key, pub_type="BKAB")
        except Publication.DoesNotExist:
            raise CommandError(f"Book not in the database: {key!r}. "
                               "Run load_books_about_oakeshott first.")
    book = data.HOSTS[key]
    publisher = (get_publisher(book["publisher"], data.PUBLISHERS,
                               book.get("city"))
                 if book.get("publisher") else None)
    host, is_new = Publication.objects.get_or_create(
        title=book["title"], year=book["year"], pub_type="MENT",
        defaults={"publisher": publisher,
                  "city": "" if publisher else book.get("city", "")})
    if is_new:
        add_people(host, book)
    return host


class Command(BaseCommand):
    help = "Load the Short Works About Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created = updated = 0
        works = ([(item, "journal") for item in data.ARTICLES] +
                 [(item, "chapter") for item in data.CHAPTERS])
        for item, kind in works:
            fields = {f: item.get(f, "") for f in
                      ("volume", "issue", "day", "month", "pages")}
            if kind == "journal":
                journal, _ = Journal.objects.get_or_create(
                    name=item["journal"])
                key = {"journal": journal}
                year = item["year"]
            else:
                host = get_host(item["book"])
                key = {"collection": host}
                year = item.get("year", host.year)
            pub, is_new = Publication.objects.get_or_create(
                title=item["title"], year=year, pub_type="SWAB", **key,
                defaults=fields)
            if is_new:
                created += 1
                add_people(pub, item)
            subject, _ = Subject.objects.get_or_create(name=item["subject"])
            if pub.subject_id != subject.id:
                pub.subject = subject
                pub.save(update_fields=["subject"])
                updated += 1
        self.stdout.write(f"Added {created} short works "
                          f"({len(works) - created} already present); "
                          f"set subject on {updated}.")
