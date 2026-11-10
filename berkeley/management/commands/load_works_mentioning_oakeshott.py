"""Load the "Works Mentioning Oakeshott" entries into the database.

These are works on other subjects that have something of substance to
say about Oakeshott. The data, and where it comes from, is in
_works_mentioning.py; each entry's abstract (in _abstracts.py, applied
by load_abstracts) says how it deals with Oakeshott.

BOOKS are whole books. ARTICLES are linked to a Journal. CHAPTERS are
linked (Publication.collection) to their book: a Books About or Books
by Oakeshott entry, a Works Mentioning entry already in the database,
or a key into HOSTS (stored as Works Mentioning, like BOOKS).

Safe to re-run: books are matched on title and year, articles and
chapters on title, year and journal or book. Subjects and links are
applied on every run.

    python manage.py load_works_mentioning_oakeshott
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import Subject, UNKNOWN_ID

from . import _works_mentioning as data
from ._loaders import load_short_works, make_book


class Command(BaseCommand):
    help = "Load the Works Mentioning Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created = updated = 0
        for book in data.BOOKS:
            _, is_new, changed = make_book(book, data, "MENT")
            created += is_new
            updated += changed and not is_new
        c, u, total = load_short_works(data, "MENT",
                                       ("BKAB", "BKBY", "MENT"))
        created += c
        updated += u
        total += len(data.BOOKS)
        self.stdout.write(f"Added {created} works mentioning Oakeshott "
                          f"({total - created} already present); "
                          f"set subject on {updated}.")
