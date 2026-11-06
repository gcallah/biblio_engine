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
every short work and host book, new or existing, so re-running picks up
edits to them.

    python manage.py load_short_works_about_oakeshott
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import Subject, UNKNOWN_ID

from . import _short_works_about as data
from ._loaders import load_short_works


class Command(BaseCommand):
    help = "Load the Short Works About Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created, updated, total = load_short_works(data, "SWAB", "BKAB")
        self.stdout.write(f"Added {created} short works "
                          f"({total - created} already present); "
                          f"set subject on {updated}.")
