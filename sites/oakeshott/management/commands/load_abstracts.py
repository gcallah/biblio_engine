"""Apply abstracts (from _abstracts.py) to entries already in the database.

Each abstract paraphrases the online description at its source URL.
Entries are matched on title, year and "where": the journal name, "in:
<book title>" for a chapter, or the publisher name for a book. Run it
after the other loaders; it only fills blank abstracts, so an editor's
changes are kept and re-running sets nothing new.

    python manage.py load_abstracts
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.management.commands._loaders import apply_abstracts

from ._abstracts import ABSTRACTS


class Command(BaseCommand):
    help = "Apply abstracts to existing entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        updated = apply_abstracts(ABSTRACTS)
        self.stdout.write(f"Set {updated} abstracts "
                          f"({len(ABSTRACTS) - updated} unchanged).")
