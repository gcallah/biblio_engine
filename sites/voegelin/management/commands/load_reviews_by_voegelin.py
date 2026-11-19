"""Load Voegelin's book reviews as "Book Reviews by Voegelin" (RVBY), in
their first publication, each linked ("Reprinted in") to the Collected
Works volume that reprints it. The data and its sources are in
_reviews_by.py; run load_books_by_voegelin first.

The reviewed book is not stored as a Publication: its title goes in
Publication.review, its authors as written in Publication.reviewed_names,
and its authors as people in Publication.reviewees (searchable as
"Reviewed author").

Safe to re-run: a review is matched on journal, year, reviewed title and
pages; fields are only filled where blank and links only added, since
editors may change entries on the site. The doubts in QUESTIONS become
open questions on the editors' to-do page.

    python manage.py load_reviews_by_voegelin \
        --settings=mysite.settings_voegelin
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import (
    Journal, OpenQuestion, Publication, Subject, UNKNOWN_ID)
from berkeley.management.commands._loaders import (
    add_missing, fill_blanks, get_person, get_reviewer, set_subject)

from . import _reviews_by as data
from ._books_by import BOOKS, VOEGELIN

BOOK_TITLES = {b["key"]: b["title"] for b in BOOKS}
FIELDS = ("title", "volume", "issue", "day", "month", "language")


def reprinting_books(item):
    """The Books by Voegelin that reprint the review."""
    books = []
    for key in item.get("reprinted", []):
        try:
            books.append(Publication.objects.get(title=BOOK_TITLES[key],
                                                 pub_type="BKBY"))
        except Publication.DoesNotExist:
            raise CommandError(f"Book not in the database: {key}. "
                               "Run load_books_by_voegelin first.")
    return books


class Command(BaseCommand):
    help = "Load the Book Reviews by Voegelin entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        keys = [r["key"] for r in data.REVIEWS]
        dupes = {k for k in keys if keys.count(k) > 1}
        if dupes:
            raise CommandError(f"duplicate keys in _reviews_by.py: {dupes}")
        voegelin = get_person(VOEGELIN)
        created = updated = links = 0
        by_key = {}
        for item in data.REVIEWS:
            journal, _ = Journal.objects.get_or_create(name=item["journal"])
            fields = {f: item.get(f, "") for f in FIELDS}
            fields["reviewed_names"] = item["names"]
            pub, is_new = Publication.objects.get_or_create(
                pub_type="RVBY", journal=journal, year=item["year"],
                review=item["book"], pages=item.get("pages", ""),
                defaults=fields)
            by_key[item["key"]] = pub
            changed = set_subject(pub, item["subject"])
            # fill blank fields only: editors may have changed the rest
            if not is_new and fill_blanks(pub, fields):
                changed = True
            if not pub.authors.exists():
                pub.authors.add(voegelin)
            if add_missing(pub.reviewees,
                           [get_reviewer(n) for n in item["reviewees"]]):
                changed = True
            if add_missing(pub.reprinted_in, reprinting_books(item)):
                links += 1
            created += is_new
            updated += changed and not is_new
        questions = 0
        for title, (details, qkeys) in data.QUESTIONS.items():
            question, is_new = OpenQuestion.objects.get_or_create(
                title=title, defaults={"details": details})
            questions += is_new
            add_missing(question.entries, [by_key[k] for k in qkeys])
        total = len(data.REVIEWS)
        self.stdout.write(f"Added {created} reviews by Voegelin "
                          f"({total - created} already present); updated "
                          f"{updated}; added reprint links to {links}; "
                          f"added {questions} open questions.")
