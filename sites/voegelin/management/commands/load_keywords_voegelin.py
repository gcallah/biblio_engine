"""Tag the Voegelin books with keywords: the books whose subject a
keyword plainly names. More tagging is done by editors on the site.

Safe to re-run: keywords are matched on their names, and tags are only
added, never removed (an editor may have changed them). Run
load_books_by_voegelin first.

    python manage.py load_keywords_voegelin \
        --settings=mysite.settings_voegelin
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import Keyword, Publication
from berkeley.management.commands._loaders import add_missing

from ._books_by import BOOKS

BOOK_TITLES = {b["key"]: b["title"] for b in BOOKS}

# keyword: keys of books in _books_by.py
KEYWORDS = {
    "Gnosticism": ["wpg", "spg_1968", "cw05", "gottesmord"],
    "political religions": ["pol_rel_de", "pol_rel_en", "cw05"],
    "anamnesis": ["anamnesis_de", "anamnesis_en", "cw06"],
    "Plato": ["oh3", "plato_1966", "cw16", "og6"],
    "Aristotle": ["oh3", "cw16", "og7"],
    "modernity": ["cw05"],
    "Enlightenment": ["enlight_rev"],
    # no books yet: tagged by editors
    "the ground": [],
    "the beyond": [],
    "ideology": [],
}


class Command(BaseCommand):
    help = "Tag the Voegelin books with keywords (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        tags = 0
        for name, keys in KEYWORDS.items():
            keyword, _ = Keyword.objects.get_or_create(name=name)
            for key in keys:
                try:
                    pub = Publication.objects.get(title=BOOK_TITLES[key],
                                                  pub_type="BKBY")
                except Publication.DoesNotExist:
                    raise CommandError(f"Book not in the database: {key}. "
                                       "Run load_books_by_voegelin first.")
                tags += add_missing(pub.keywords, [keyword])
        self.stdout.write(f"Added {tags} keyword tags.")
