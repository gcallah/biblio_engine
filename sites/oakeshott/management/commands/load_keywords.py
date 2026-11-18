"""Attach keywords (from _keywords.py) to entries already in the database.

BOOK_KEYWORDS go to the book and to every review of it; ENTRY_KEYWORDS
go to single entries, matched on title, reviewed title, year and
"where" (as in load_abstracts). Run it after the other loaders; it only
adds links, so re-running adds nothing new.

    python manage.py load_keywords
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Keyword, Publication

from ._keywords import BOOK_KEYWORDS, ENTRY_KEYWORDS, KEYWORDS
from .load_abstracts import where


def one(matches, label):
    if len(matches) != 1:
        raise CommandError(f"{len(matches)} entries match {label}")
    return matches[0]


class Command(BaseCommand):
    help = "Attach keywords to existing entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        kw = {name: Keyword.objects.get_or_create(name=name)[0]
              for name in KEYWORDS}
        added = 0

        def tag(pub, names):
            nonlocal added
            have = set(pub.keywords.values_list("name", flat=True))
            for name in names:
                if name not in kw:
                    raise CommandError(f"Unknown keyword {name!r}")
                if name not in have:
                    pub.keywords.add(kw[name])
                    added += 1

        for title, names in BOOK_KEYWORDS.items():
            book = one(list(Publication.objects.filter(
                title=title, pub_type__startswith="BK")), repr(title))
            tag(book, names)
            for review in Publication.objects.filter(pub_reviewed=book):
                tag(review, names)

        for (title, review, year, place), names in ENTRY_KEYWORDS.items():
            pubs = Publication.objects.filter(
                title=title, review=review, year=year).select_related(
                    "journal", "collection", "publisher")
            tag(one([p for p in pubs if where(p) == place],
                    f"{title or review!r} ({year}, {place!r})"), names)

        self.stdout.write(f"Added {added} keyword links.")
