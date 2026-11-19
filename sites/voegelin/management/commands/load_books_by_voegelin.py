"""Load the "Books by Voegelin" entries: his books in German and English,
their translations into the other language, and the 34 volumes of The
Collected Works of Eric Voegelin. The data is in _books_by.py.

Safe to re-run: people and publishers are matched on their names and
books on title and year, so running it twice adds nothing. Fields are
only filled where blank, and links (translators, editors, "translation
of", "reprinted in") only added, since editors may change entries on the
site. The doubts in QUESTIONS become open questions on the editors' to-do
page.

    python manage.py load_books_by_voegelin \
        --settings=mysite.settings_voegelin
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import (
    Authorship, Editorship, OpenQuestion, Publication, Subject, UNKNOWN_ID,
)
from berkeley.management.commands._loaders import (
    add_missing, fill_blanks, get_person, get_publisher)

from ._books_by import BOOKS, PEOPLE, PUBLISHERS, QUESTIONS, VOEGELIN


def author(name):
    """An authors entry: "V" for Voegelin, else a key of PEOPLE."""
    return VOEGELIN if name == "V" else PEOPLE[name]


class Command(BaseCommand):
    help = "Load the Books by Voegelin entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        keys = [b["key"] for b in BOOKS]
        dupes = {k for k in keys if keys.count(k) > 1}
        if dupes:
            raise ValueError(f"duplicate keys in _books_by.py: {dupes}")
        by_key = {}
        created = updated = 0
        for book in BOOKS:
            pub, is_new = Publication.objects.get_or_create(
                title=book["title"], year=book["year"], pub_type="BKBY",
                defaults={"publisher": get_publisher(
                    book["publisher"], PUBLISHERS, book.get("city"))})
            by_key[book["key"]] = pub
            if fill_blanks(pub, {"language": book.get("language", ""),
                                 "isbn": book.get("isbn", "")}):
                updated += 1
            if is_new:
                created += 1
                for pos, name in enumerate(book.get("authors", ["V"]), 1):
                    Authorship.objects.create(
                        publication=pub, person=get_person(author(name)),
                        position=pos)
                for pos, name in enumerate(book.get("editors", []), 1):
                    Editorship.objects.create(publication=pub,
                                              person=get_person(name),
                                              position=pos)
            add_missing(pub.translators,
                        [get_person(n) for n in book.get("translators", [])])
        # links between books, once they all exist
        links = 0
        for book in BOOKS:
            pub = by_key[book["key"]]
            original = book.get("translation_of")
            if original and fill_blanks(
                    pub, {"translation_of": by_key[original]}):
                links += 1
            for key in book.get("reprints", []):
                if add_missing(by_key[key].reprinted_in, [pub]):
                    links += 1
        # open questions for the editors' to-do page
        questions = 0
        for title, (details, keys) in QUESTIONS.items():
            question, is_new = OpenQuestion.objects.get_or_create(
                title=title, defaults={"details": details})
            questions += is_new
            add_missing(question.entries, [by_key[k] for k in keys])
        self.stdout.write(f"Added {created} books "
                          f"({len(BOOKS) - created} already present); "
                          f"filled fields on {updated}; added {links} "
                          f"links and {questions} open questions.")
