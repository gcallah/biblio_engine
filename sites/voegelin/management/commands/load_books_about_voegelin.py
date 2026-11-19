"""Load the "Books About Voegelin", and books that build on his thought
without being about him ("Works Mentioning Voegelin"), first editions.

Source: the Eric Voegelin Institute's list of books
(faculty.lsu.edu/voegelin/voegelins-works/books.php), checked against
Open Library and Library of Congress records. Of the books listed there,
those already in the database as Books by Voegelin (the Collected Works,
the letters with Strauss and Heilman, the Reader) and the series volumes
on other subjects are left out. Tradition v. Rationalism, in the
Oakeshott bibliography, is about Voegelin too.

Safe to re-run: people and publishers are matched on their names and
books on title and year; subjects only fill blanks (see make_book).

    python manage.py load_books_about_voegelin \
        --settings=mysite.settings_voegelin
"""
import sys

from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import Subject, UNKNOWN_ID
from berkeley.management.commands._loaders import make_book

POL, PHIL, LIT, REL = "Politics", "Philosophy", "Literature", "Religion"

# (first, middle, last)
COOPER = ("Barry", "", "Cooper")
TREPANIER = ("Lee", "", "Trepanier")
VON_HEYKING = ("John", "", "von Heyking")

PUBLISHERS = {
    "University of Missouri Press": ("Columbia", "MO"),
    "Lexington Books": ("Lanham", "MD"),
}

MISSOURI = "University of Missouri Press"

BOOKS_ABOUT = [
    dict(title="Voegelin, Schelling, and the Philosophy of Historical "
               "Existence",
         year=2003, publisher=MISSOURI, authors=[("Jerry", "", "Day")],
         subject=PHIL),
    dict(title="Eric Voegelin and the Problem of Christian Political Order",
         year=2007, publisher=MISSOURI,
         authors=[("Jeffrey", "C.", "Herndon")], subject=REL),
    dict(title="The Philosopher and the Storyteller: Eric Voegelin and "
               "Twentieth-Century Literature",
         year=2008, publisher=MISSOURI,
         authors=[("Charles", "R.", "Embry")], subject=LIT),
    # interviews with people who knew him; Open Library also lists 2007
    # (the catalogue record's year), the book is dated 2008
    dict(title="Voegelin Recollected: Conversations on a Life",
         year=2008, publisher=MISSOURI,
         editors=[COOPER, ("Jodi", "", "Bruhn")], subject=PHIL),
    dict(title="Beginning the Quest: Law and Politics in the Early Work of "
               "Eric Voegelin",
         year=2009, publisher=MISSOURI, authors=[COOPER], subject=POL),
    # the LSU list spells the co-editor "Stephen"
    dict(title="Eric Voegelin and the Continental Tradition: Explorations "
               "in Modern Political Thought",
         year=2011, publisher=MISSOURI,
         editors=[TREPANIER, ("Steven", "F.", "McGuire")], subject=PHIL),
    dict(title="Tradition v. Rationalism: Voegelin, Oakeshott, Hayek, "
               "and Others",
         year=2018, publisher="Lexington Books",
         editors=[TREPANIER, ("Gene", "", "Callahan")], subject=PHIL),
]

# built on Voegelin's thought, but not about him
MENTIONING = [
    dict(title="Transcendence and History: The Search for Ultimacy from "
               "Ancient Societies to Postmodernity",
         year=2003, publisher=MISSOURI, authors=[("Glenn", "", "Hughes")],
         subject=PHIL),
    dict(title="New Political Religions, or An Analysis of Modern "
               "Terrorism",
         year=2004, publisher=MISSOURI, authors=[COOPER], subject=POL),
    dict(title="Etty Hillesum and the Flow of Presence: A Voegelinian "
               "Analysis",
         year=2008, publisher=MISSOURI,
         authors=[("Meins", "G. S.", "Coetsier")], subject=REL),
    # includes chapters on Voegelin
    dict(title="Teaching in an Age of Ideology",
         year=2012, publisher="Lexington Books",
         editors=[VON_HEYKING, TREPANIER], subject=PHIL),
]


class Command(BaseCommand):
    help = "Load the Books About Voegelin entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        data = sys.modules[__name__]
        counts = {}
        for books, pub_type in ((BOOKS_ABOUT, "BKAB"), (MENTIONING, "MENT")):
            counts[pub_type] = sum(make_book(b, data, pub_type)[1]
                                   for b in books)
        self.stdout.write(
            f"Added {counts['BKAB']} books about Voegelin "
            f"({len(BOOKS_ABOUT) - counts['BKAB']} already present) and "
            f"{counts['MENT']} works mentioning him "
            f"({len(MENTIONING) - counts['MENT']} already present).")
