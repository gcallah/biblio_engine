"""Load reviews of Oakeshott's books as "Book Reviews of Books by
Oakeshott" (RVOB).

The data and its source are in _reviews_of_books_by.py. Each review is
linked (Publication.pub_reviewed) to the Books by Oakeshott entry it
reviews, so run load_books_by_oakeshott first. Oakeshott is its
reviewee, so a "Reviewed author" search for him finds it. Its subject is
the reviewed book's.

Reviewers are matched to people already in the database on last name
and first initial (so "R. A. D. Grant" is "Robert Grant"), unless both
have middle initials and they differ.

Safe to re-run: a review is matched on journal, year, volume, date and
pages. Titles, issues, URLs, book links, subjects and reviewees are applied
on every run.

    python manage.py load_reviews_of_books_by_oakeshott
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Journal, Publication, Subject, UNKNOWN_ID

from . import _reviews_of_books_by as data
from ._loaders import get_person, get_reviewer

KEY = ("volume", "day", "month", "pages")
FIELDS = ("title", "issue", "url")


class Command(BaseCommand):
    help = "Load the Book Reviews of Books by Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        oakeshott = get_person(data.OAKESHOTT)
        created = updated = 0
        for item in data.REVIEWS:
            try:
                book = Publication.objects.get(title=item["book"],
                                               pub_type="BKBY")
            except Publication.DoesNotExist:
                raise CommandError(f"Book not in the database: "
                                   f"{item['book']!r}. Run "
                                   "load_books_by_oakeshott first.")
            journal, _ = Journal.objects.get_or_create(name=item["journal"])
            key = {f: item.get(f, "") for f in KEY}
            fields = {f: item.get(f, "") for f in FIELDS}
            fields["pub_reviewed"] = book
            fields["subject_id"] = book.subject_id
            pub, is_new = Publication.objects.get_or_create(
                pub_type="RVOB", journal=journal, year=item["year"], **key,
                defaults=fields)
            changed = False
            if not is_new:
                stale = [f for f, v in fields.items() if getattr(pub, f) != v]
                for f in stale:
                    setattr(pub, f, fields[f])
                if stale:
                    pub.save(update_fields=stale)
                    changed = True
            if is_new:
                for pos, name in enumerate(item["authors"], 1):
                    pub.authorship_set.create(person=get_reviewer(name),
                                              position=pos)
            if list(pub.reviewees.all()) != [oakeshott]:
                pub.reviewees.set([oakeshott])
                changed = True
            created += is_new
            updated += changed and not is_new
        total = len(data.REVIEWS)
        self.stdout.write(f"Added {created} reviews of books by Oakeshott "
                          f"({total - created} already present); "
                          f"updated {updated}.")
