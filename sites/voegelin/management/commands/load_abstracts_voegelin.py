"""Apply abstracts (from _abstracts.py) to Voegelin entries already in
the database.

Each abstract paraphrases a source at its URL: the publisher's
description or abstract, a library catalogue note, the volume's own
introduction, or the piece's own open text; its "basis" says which. No
abstract is written from thin evidence, and none from third-party
reviews or unauthorised copies. Entries are matched on title, year and
"where": the journal name, "in: <book title>" for a chapter, or the
publisher name for a book. Run it after the other loaders; it only fills
blank abstracts, so an editor's changes are kept and re-running sets
nothing new. The doubts in _abstract_questions.py, noticed while
searching, become open questions on the editors' to-do page.

    python manage.py load_abstracts_voegelin \
        --settings=mysite.settings_voegelin
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.management.commands._loaders import (
    add_questions, apply_abstracts)

from ._abstract_questions import QUESTIONS
from ._abstracts import ABSTRACTS


class Command(BaseCommand):
    help = "Apply abstracts to existing Voegelin entries (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        updated = apply_abstracts(ABSTRACTS)
        questions = add_questions(QUESTIONS)
        self.stdout.write(f"Set {updated} abstracts "
                          f"({len(ABSTRACTS) - updated} unchanged); "
                          f"added {questions} open questions.")
