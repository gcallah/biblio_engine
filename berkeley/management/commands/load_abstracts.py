"""Apply abstracts (from _abstracts.py) to entries already in the database.

Each abstract paraphrases the online description at its source URL.
Entries are matched on title, year and "where": the journal name, "in:
<book title>" for a chapter, or the publisher name for a book. Run it
after the other loaders; re-running only rewrites abstracts that changed.

    python manage.py load_abstracts
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Publication

from ._abstracts import ABSTRACTS
from ._loaders import fill_blanks

MAX_LEN = Publication._meta.get_field("abstract").max_length


def where(pub):
    if pub.journal_id:
        return pub.journal.name
    if pub.collection_id:
        return "in: " + pub.collection.title
    return pub.publisher.name if pub.publisher_id else ""


class Command(BaseCommand):
    help = "Apply abstracts to existing entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        updated = 0
        for (title, year, place), info in ABSTRACTS.items():
            if len(info["abstract"]) > MAX_LEN:
                raise CommandError(f"Abstract too long: {title!r}")
            matches = [p for p in Publication.objects.filter(
                title=title, year=year).select_related(
                    "journal", "collection", "publisher")
                if where(p) == place]
            if len(matches) != 1:
                raise CommandError(f"{len(matches)} entries match "
                                   f"{title!r} ({year}, {place!r})")
            pub = matches[0]
            # never overwrite an abstract an editor has written or changed
            if fill_blanks(pub, {"abstract": info["abstract"]}):
                updated += 1
        self.stdout.write(f"Set {updated} abstracts "
                          f"({len(ABSTRACTS) - updated} unchanged).")
