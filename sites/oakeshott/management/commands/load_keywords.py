"""Attach keywords (from _keywords.py) to entries already in the database.

BOOK_KEYWORDS go to the book and to every review of it; ENTRY_KEYWORDS
go to single entries, matched on title, reviewed title, year and
"where" (as in load_abstracts); the second set (…_2) the same way.
POSSIBLE becomes open questions on the editors' to-do page. Run it after
the other loaders; it only adds links and questions, so re-running adds
nothing new.

    python manage.py load_keywords
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Keyword, OpenQuestion, Publication

from ._keywords import (
    BOOK_KEYWORDS, BOOK_KEYWORDS_2, ENTRY_KEYWORDS, ENTRY_KEYWORDS_2, KEYWORDS,
    POSSIBLE)
from .load_abstracts import where


def one(matches, label):
    if len(matches) != 1:
        raise CommandError(f"{len(matches)} entries match {label}")
    return matches[0]


def find(key):
    """The entry a BOOK_KEYWORDS title or ENTRY_KEYWORDS key names."""
    if isinstance(key, str):
        return one(list(Publication.objects.filter(
            title=key, pub_type__startswith="BK")), repr(key))
    title, review, year, place = key
    pubs = Publication.objects.filter(
        title=title, review=review, year=year).select_related(
            "journal", "collection", "publisher")
    return one([p for p in pubs if where(p) == place],
               f"{title or review!r} ({year}, {place!r})")


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

        for books in (BOOK_KEYWORDS, BOOK_KEYWORDS_2):
            for title, names in books.items():
                book = find(title)
                tag(book, names)
                for review in Publication.objects.filter(pub_reviewed=book):
                    tag(review, names)

        for entries in (ENTRY_KEYWORDS, ENTRY_KEYWORDS_2):
            for key, names in entries.items():
                tag(find(key), names)

        questions = 0
        for title, (details, keys) in POSSIBLE.items():
            question, is_new = OpenQuestion.objects.get_or_create(
                title=title, defaults={"details": details})
            questions += is_new
            have = set(question.entries.all())
            question.entries.add(*[p for p in map(find, keys)
                                   if p not in have])

        self.stdout.write(f"Added {added} keyword links and {questions} "
                          "open questions.")
