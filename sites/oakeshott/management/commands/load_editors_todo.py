"""Load the editors' to-do list: the possible entries (Candidate) and the
open questions (OpenQuestion) shown on the editors' to-do page.

The possible entries come from docs/works_mentioning_triage.csv, the
sorting of MOA's "other works" list. Once loaded, the live database is
where editors keep this list up to date (through the admin); the CSV is
only its starting point and is not read again for rows already loaded.

Safe to re-run: candidates are matched on their MOA line and questions on
their title, and existing ones are never changed, so an editor's
decisions are kept.

    python manage.py load_editors_todo
"""
import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from berkeley.models import Candidate, OpenQuestion, Publication

from ._short_works_about import OBIT

TRIAGE_CSV = Path(settings.BASE_DIR) / "docs" / "works_mentioning_triage.csv"

# the triage CSV's decisions, as candidate statuses
STATUSES = {
    "edge": Candidate.UNDECIDED,
    "left out: not checked": Candidate.NOT_CHECKED,
    "left out: not a new work": Candidate.LEFT_OUT,
    "left out: passing mention": Candidate.LEFT_OUT,
}

# Open questions: (title, details, how to find the entries it concerns)
QUESTIONS = [
    ("Are the three Daily Telegraph obituaries (21 December 1990) one "
     "piece?",
     "MOA lists three Daily Telegraph obituaries of Oakeshott for 21 "
     "December 1990, p. 19: one anonymous, one by J. Casey and one by "
     "P. Worsthorne. They are entered as three separate Short Works About "
     "entries. If MOA listed one obituary under each contributor, they "
     "should be merged into one entry with all its authors.",
     dict(title=OBIT, journal__name="Daily Telegraph", year=1990,
          month="December", day="21")),
]


class Command(BaseCommand):
    help = "Load the editors' to-do list: possible entries and open " \
           "questions (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        added = 0
        with open(TRIAGE_CSV, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                decision = row["decision"]
                status = STATUSES.get(decision, Candidate.ADDED)
                reason = row["reason"]
                if status == Candidate.ADDED:   # e.g. "review (loaded)"
                    reason = f"{decision}. {reason}"
                elif status == Candidate.NOT_CHECKED:
                    reason = ""     # "not researched; left out by default"
                _, is_new = Candidate.objects.get_or_create(
                    moa_line=int(row["moa_line"]),
                    defaults=dict(author=row["author"],
                                  citation=row["citation"], status=status,
                                  reason=reason, evidence=row["evidence"],
                                  research_id=row["research_id"]))
                added += is_new
        questions = 0
        for title, details, entries in QUESTIONS:
            question, is_new = OpenQuestion.objects.get_or_create(
                title=title, defaults={"details": details})
            if is_new:
                question.entries.set(Publication.objects.filter(**entries))
                questions += 1
        self.stdout.write(f"Added {added} possible entries and {questions} "
                          "open questions.")
