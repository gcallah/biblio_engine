"""Load the "Short Works by Voegelin": his essays, articles and chapters
in their first publication, each linked ("Reprinted in") to the
Collected Works volume or other book of his that reprints it. The data
is in _short_works_by.py; run load_books_by_voegelin first.

Safe to re-run: works are matched on title, year and journal or host
book, fields are only filled where blank and links only added (see
load_short_works), since editors may change entries on the site. The
doubts in QUESTIONS become open questions on the editors' to-do page.

    python manage.py load_short_works_by_voegelin \
        --settings=mysite.settings_voegelin
"""
from types import SimpleNamespace

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import OpenQuestion, Publication, Subject, UNKNOWN_ID
from berkeley.management.commands._loaders import (
    add_missing, fill_blanks, load_short_works)

from . import _short_works_by as raw
from ._books_by import BOOKS, VOEGELIN

BOOK_TITLES = {b["key"]: b["title"] for b in BOOKS}


def with_names(item):
    """item with "V" in its authors replaced by Voegelin's name."""
    return dict(item, authors=[VOEGELIN if a == "V" else tuple(a)
                               for a in item.get("authors", ["V"])])


# the data as load_short_works expects it
data = SimpleNamespace(
    PUBLISHERS=raw.PUBLISHERS, HOSTS=raw.HOSTS,
    ARTICLES=[with_names(i) for i in raw.ARTICLES],
    CHAPTERS=[with_names(i) for i in raw.CHAPTERS])


def find(item):
    """The entry load_short_works made for item."""
    where = ({"journal__name": item["journal"]} if "journal" in item else
             {"collection__title": data.HOSTS[item["book"]]["title"]})
    return Publication.objects.get(title=item["title"], year=item["year"],
                                   pub_type="SWBY", **where)


class Command(BaseCommand):
    help = "Load the Short Works by Voegelin entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created, updated, total = load_short_works(data, "SWBY", "BKBY")
        links = 0
        by_key = {}
        for item in data.ARTICLES + data.CHAPTERS:
            pub = by_key[item["key"]] = find(item)
            fill_blanks(pub, {"language": item.get("language", "")})
            books = []
            for key in item.get("reprinted", []):
                try:
                    books.append(Publication.objects.get(
                        title=BOOK_TITLES[key], pub_type="BKBY"))
                except Publication.DoesNotExist:
                    raise CommandError(f"Book not in the database: {key}. "
                                       "Run load_books_by_voegelin first.")
            links += add_missing(pub.reprinted_in, books)
        questions = 0
        for title, (details, keys) in raw.QUESTIONS.items():
            question, is_new = OpenQuestion.objects.get_or_create(
                title=title, defaults={"details": details})
            questions += is_new
            add_missing(question.entries, [by_key[k] for k in keys])
        self.stdout.write(f"Added {created} short works by Voegelin "
                          f"({total - created} already present); updated "
                          f"{updated}; added reprint links to {links}; "
                          f"added {questions} open questions.")
