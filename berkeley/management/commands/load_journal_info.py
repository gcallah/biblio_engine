"""Apply journal details (from _journal_info.py) to journals already in
the database: a short description (about one paragraph, so the hover
popup in the results table stays small) and a URL for the journal's
site, or a reference page for journals no longer published.

Journals are matched on their exact name. Fields left empty in
_journal_info.py are not touched. Re-running changes nothing.

    python manage.py load_journal_info
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Journal

from ._journal_info import JOURNAL_INFO

FIELDS = ("descr", "url")
MAX_LEN = {f: Journal._meta.get_field(f).max_length for f in FIELDS}


class Command(BaseCommand):
    help = "Apply journal descriptions and URLs (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        updated = 0
        for name, info in JOURNAL_INFO.items():
            for field, limit in MAX_LEN.items():
                if len(info.get(field) or "") > limit:
                    raise CommandError(f"{field} too long for {name}")
            matches = list(Journal.objects.filter(name=name))
            if len(matches) != 1:
                raise CommandError(f"{len(matches)} journals named {name}")
            journal = matches[0]
            changed = [f for f in FIELDS
                       if info.get(f) and getattr(journal, f) != info[f]]
            for field in changed:
                setattr(journal, field, info[field])
            if changed:
                journal.save(update_fields=changed)
                updated += 1
        self.stdout.write(f"Updated {updated} journals "
                          f"({len(JOURNAL_INFO) - updated} unchanged).")
