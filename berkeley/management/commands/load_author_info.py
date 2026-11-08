"""Apply author details (from _author_info.py) to people already in the
database: affiliation, years of birth and death, a short description
and a URL for a page about the person (e.g. Wikipedia).

People are matched on (last name, first name, middle name). Fields left
empty in _author_info.py are not touched, so a later lookup can fill
them in. Run it after the other loaders; re-running changes nothing.

    python manage.py load_author_info
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Person

from ._author_info import AUTHOR_INFO

FIELDS = ("affiliation", "yob", "yod", "descr", "url")
MAX_LEN = {f: Person._meta.get_field(f).max_length
           for f in ("affiliation", "descr", "url")}


class Command(BaseCommand):
    help = ("Apply author affiliations, years, descriptions and URLs "
            "(idempotent).")

    @transaction.atomic
    def handle(self, *args, **options):
        updated = 0
        for (lname, fname, mname), info in AUTHOR_INFO.items():
            for field, limit in MAX_LEN.items():
                if len(info.get(field) or "") > limit:
                    raise CommandError(f"{field} too long for {lname}")
            matches = [p for p in Person.objects.filter(lname=lname,
                                                        fname=fname)
                       if (p.mname or "") == mname]
            if len(matches) != 1:
                raise CommandError(f"{len(matches)} people match "
                                   f"{fname} {mname} {lname}")
            person = matches[0]
            changed = [f for f in FIELDS
                       if info.get(f) and getattr(person, f) != info[f]]
            for field in changed:
                setattr(person, field, info[field])
            if changed:
                person.save(update_fields=changed)
                updated += 1
        self.stdout.write(f"Updated {updated} people "
                          f"({len(AUTHOR_INFO) - updated} unchanged).")
