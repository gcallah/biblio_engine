"""Load the "Books by Oakeshott" entries into the database.

Safe to re-run: people and publishers are matched on their names,
and books on title and year, so running it twice does not create duplicates.
Subjects and abstracts (from book_info.py) are applied to every book,
new or existing, so re-running picks up edits to them.

    python manage.py load_books_by_oakeshott
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import (
    Authorship, Editorship, Publication, Subject, UNKNOWN_ID,
)

from ._loaders import get_person, get_publisher
from .book_info import BOOK_INFO

# (first, middle, last)
OAKESHOTT = ("Michael", "", "Oakeshott")
GRIFFITH = ("Guy", "", "Griffith")
FULLER = ("Timothy", "", "Fuller")
LETWIN = ("Shirley", "Robin", "Letwin")
OSULLIVAN = ("Luke", "", "O'Sullivan")
NARDIN = ("Terry", "", "Nardin")

# name: (usual city, province). A book can override the city with
# "city"; the same press in a different city is stored as its own
# Publisher, since citations take the place from the publisher's address.
PUBLISHERS = {
    "Cambridge University Press": ("Cambridge", "England"),
    "Faber & Faber": ("London", "England"),
    "Bowes & Bowes": ("London", "England"),
    "Methuen": ("London", "England"),
    "Basil Blackwell": ("Oxford", "England"),
    "Clarendon Press": ("Oxford", "England"),
    "Yale University Press": ("New Haven", "CT"),
    "Imprint Academic": ("Exeter", "England"),
    "Liberty Fund": ("Indianapolis", "IN"),
}

BOOKS = [
    dict(title="Experience and Its Modes", year=1933,
         publisher="Cambridge University Press"),
    dict(title="The Social and Political Doctrines of Contemporary Europe",
         year=1939, publisher="Cambridge University Press"),
    dict(title="A Guide to the Classics, or How to Pick the Derby Winner",
         year=1936, publisher="Faber & Faber",
         authors=[OAKESHOTT, GRIFFITH]),
    dict(title="A New Guide to the Derby: How to Pick the Winner", year=1947,
         publisher="Faber & Faber", authors=[OAKESHOTT, GRIFFITH]),
    dict(title="Political Education: An Inaugural Lecture", year=1951,
         publisher="Bowes & Bowes", city="Cambridge"),
    dict(title="The Voice of Poetry in the Conversation of Mankind: An Essay",
         year=1959, publisher="Bowes & Bowes"),
    dict(title="Rationalism in Politics and Other Essays", year=1962,
         publisher="Methuen"),
    dict(title="On Human Conduct", year=1975, publisher="Clarendon Press"),
    dict(title="Hobbes on Civil Association", year=1975,
         publisher="Basil Blackwell"),
    dict(title="On History and Other Essays", year=1983,
         publisher="Basil Blackwell"),
    dict(title="Rationalism in Politics and Other Essays: "
               "New and Expanded Edition",
         year=1991, publisher="Liberty Fund", editors=[FULLER]),
    dict(title="The Voice of Liberal Learning: Michael Oakeshott on Education",
         year=1989, publisher="Yale University Press", editors=[FULLER]),
    dict(title="Morality and Politics in Modern Europe: The Harvard Lectures",
         year=1993, publisher="Yale University Press", editors=[LETWIN]),
    dict(title="Religion, Politics and the Moral Life", year=1993,
         publisher="Yale University Press", editors=[FULLER]),
    dict(title="The Politics of Faith and the Politics of Scepticism",
         year=1996, publisher="Yale University Press", editors=[FULLER]),
    dict(title="What is History? and Other Essays", year=2004,
         publisher="Imprint Academic", editors=[OSULLIVAN]),
    dict(title="Lectures in the History of Political Thought", year=2006,
         publisher="Imprint Academic", editors=[NARDIN, OSULLIVAN]),
    dict(title="The Concept of a Philosophical Jurisprudence: "
               "Essays and Reviews 1926–51",
         year=2007, publisher="Imprint Academic", editors=[OSULLIVAN]),
    dict(title="The Vocabulary of a Modern European State: "
               "Essays and Reviews 1952–88",
         year=2008, publisher="Imprint Academic", editors=[OSULLIVAN]),
    dict(title="Early Political Writings 1925–30: A Discussion of Some "
               "Matters Preliminary to the Study of Political Philosophy",
         year=2010, publisher="Imprint Academic", editors=[OSULLIVAN]),
    dict(title="Notebooks, 1922–86", year=2014,
         publisher="Imprint Academic", editors=[OSULLIVAN]),
]


class Command(BaseCommand):
    help = "Load the Books by Oakeshott entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        created = updated = 0
        for book in BOOKS:
            pub, is_new = Publication.objects.get_or_create(
                title=book["title"], year=book["year"], pub_type="BKBY",
                defaults={"publisher": get_publisher(book["publisher"],
                                                     PUBLISHERS,
                                                     book.get("city"),
                    book.get("province"))})
            info = BOOK_INFO.get(book["title"])
            if info:
                subject, _ = Subject.objects.get_or_create(
                    name=info["subject"])
                if (pub.subject_id, pub.abstract) != (subject.id,
                                                      info["abstract"]):
                    pub.subject = subject
                    pub.abstract = info["abstract"]
                    pub.save(update_fields=["subject", "abstract"])
                    updated += 1
            if not is_new:
                continue
            created += 1
            for pos, name in enumerate(book.get("authors", [OAKESHOTT]), 1):
                Authorship.objects.create(publication=pub,
                                          person=get_person(name),
                                          position=pos)
            for pos, name in enumerate(book.get("editors", []), 1):
                Editorship.objects.create(publication=pub,
                                          person=get_person(name),
                                          position=pos)
        self.stdout.write(f"Added {created} books "
                          f"({len(BOOKS) - created} already present); "
                          f"set subject/abstract on {updated}.")
