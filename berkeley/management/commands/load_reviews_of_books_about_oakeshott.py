"""Load reviews of books about Oakeshott as "Book Reviews of Books About
Oakeshott" (RVAB).

The data and its sources are in _reviews_of_books_about.py. Each review
is linked (Publication.pub_reviewed) to the Books About Oakeshott entry
it reviews, so run load_books_about_oakeshott first. Its reviewees are
the authors (or, for an edited volume, the editors) of that book and of
any other books it reviews ("also"), so a "Reviewed author" search finds
it. Its subject is the reviewed book's.

Reviewers are matched to people already in the database on last name
and first initial (so "T. Fuller" is Timothy Fuller), unless their
middle initials differ. An entry with exact=True matches its reviewers
on full first and last name instead, for an initial that would point to
the wrong person.

Safe to re-run: a review is matched on journal, year, volume, date and
pages. Titles, issues, links, book links, subjects and reviewees are
applied on every run.

    python manage.py load_reviews_of_books_about_oakeshott
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Journal, Publication, Subject, UNKNOWN_ID

from . import _reviews_of_books_about as data
from ._loaders import get_person, get_reviewer

KEY = ("volume", "day", "month", "pages")
FIELDS = ("title", "issue", "url", "doi")


def get_book(title):
    try:
        return Publication.objects.get(title=title, pub_type="BKAB")
    except Publication.DoesNotExist:
        raise CommandError(f"Book not in the database: {title!r}. Run "
                           "load_books_about_oakeshott first.")


def book_people(book):
    """Who a review of book reviews: its authors, else its editors."""
    return book.ordered_authors() or book.ordered_editors()


class Command(BaseCommand):
    help = ("Load the Book Reviews of Books About Oakeshott entries "
            "(idempotent).")

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created = updated = 0
        for item in data.REVIEWS:
            book = get_book(item["book"])
            reviewees = []
            for b in [book] + [get_book(t) for t in item.get("also", [])]:
                reviewees += [p for p in book_people(b) if p not in reviewees]
            journal, _ = Journal.objects.get_or_create(name=item["journal"])
            key = {f: item.get(f, "") for f in KEY}
            fields = {f: item.get(f, "") for f in FIELDS}
            fields["pub_reviewed"] = book
            fields["subject_id"] = book.subject_id
            pub, is_new = Publication.objects.get_or_create(
                pub_type="RVAB", journal=journal, year=item["year"], **key,
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
                match = get_person if item.get("exact") else get_reviewer
                for pos, name in enumerate(item["authors"], 1):
                    pub.authorship_set.create(person=match(name),
                                              position=pos)
            if set(pub.reviewees.all()) != set(reviewees):
                pub.reviewees.set(reviewees)
                changed = True
            created += is_new
            updated += changed and not is_new
        total = len(data.REVIEWS)
        self.stdout.write(f"Added {created} reviews of books about Oakeshott "
                          f"({total - created} already present); "
                          f"updated {updated}.")
