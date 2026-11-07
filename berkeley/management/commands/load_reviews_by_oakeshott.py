"""Load Oakeshott's book reviews as "Book Reviews by Oakeshott" (RVBY).

The data and its source are in _reviews_by.py. The reviewed book is not
stored as a Publication: its title goes in Publication.review, its
authors as written in Publication.reviewed_names, and its authors as
people in Publication.reviewees (searchable as "Reviewed author").

"reprinted" links a review to the books that reprint it
(Publication.reprinted_in): Books by Oakeshott, which must be loaded
first, or a book stored as "Works Mentioning Oakeshott".

Safe to re-run: a review is matched on journal, year, reviewed title
and pages. Subjects, reviewees and reprints are applied on every run.

    python manage.py load_reviews_by_oakeshott
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import Journal, Person, Publication, Subject, UNKNOWN_ID

from . import _reviews_by as data
from ._loaders import get_host, get_person, set_subject

FIELDS = ("title", "volume", "issue", "day", "month")


def get_reviewee(name):
    """Reuse a person already in the database when the last name and
    first initial match, so "R.G. Collingwood" does not duplicate
    "Robin George Collingwood"."""
    fname, mname, lname = name
    if fname:
        for person in Person.objects.filter(lname=lname):
            if person.fname[:1] == fname[:1]:
                return person
    return get_person(name)


class Command(BaseCommand):
    help = "Load the Book Reviews by Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        oakeshott = get_person(data.OAKESHOTT)
        created = updated = 0
        for item in data.REVIEWS:
            journal, _ = Journal.objects.get_or_create(name=item["journal"])
            fields = {f: item.get(f, "") for f in FIELDS}
            fields["reviewed_names"] = item["names"]
            pub, is_new = Publication.objects.get_or_create(
                pub_type="RVBY", journal=journal, year=item["year"],
                review=item["book"], pages=item.get("pages", ""),
                defaults=fields)
            changed = set_subject(pub, item["subject"])
            if not is_new:
                stale = [f for f, v in fields.items() if getattr(pub, f) != v]
                for f in stale:
                    setattr(pub, f, fields[f])
                if stale:
                    pub.save(update_fields=stale)
                    changed = True
            if not pub.authors.exists():
                pub.authors.add(oakeshott)
            people = [get_reviewee(n) for n in item["reviewees"]]
            if set(pub.reviewees.all()) != set(people):
                pub.reviewees.set(people)
                changed = True
            books = [get_host(key, data, "BKBY")
                     for key in item.get("reprinted", [])]
            if set(pub.reprinted_in.all()) != set(books):
                pub.reprinted_in.set(books)
                changed = True
            created += is_new
            updated += changed and not is_new
        total = len(data.REVIEWS)
        self.stdout.write(f"Added {created} reviews by Oakeshott "
                          f"({total - created} already present); "
                          f"updated {updated}.")
