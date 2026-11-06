"""Load "Short Works by Oakeshott" that can be read in full online.

The data, the full-text sources and why they were chosen are in
_short_works_by.py. Chapters link to their book: a Books by Oakeshott
entry (run load_books_by_oakeshott first) or a book stored as "Works
Mentioning Oakeshott". Safe to re-run; subjects and full-text URLs are
applied on every run.

    python manage.py load_short_works_by_oakeshott
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import Subject, UNKNOWN_ID

from . import _short_works_by as data
from ._loaders import load_short_works


class Command(BaseCommand):
    help = "Load the Short Works by Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created, updated, total = load_short_works(data, "SWBY", "BKBY")
        self.stdout.write(f"Added {created} short works by Oakeshott "
                          f"({total - created} already present); "
                          f"updated {updated}.")
