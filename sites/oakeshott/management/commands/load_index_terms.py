"""Fill the index (from _index_terms.py) for entries already in the
database, and put its doubts on the editors' to-do page.

TERMS become IndexTerms, each linked to the entries that refer to it;
POSSIBLE become PossibleIndexTerms (a term that might be added, or
entries that might belong under a term already there). Entries are
matched as in load_keywords. It only adds terms and links, so re-running
adds nothing new; a link an editor removed comes back if the loader
is run again. The data was drafted from the live database, so in a
from-scratch build (bin/load_data.sh) entries the editors added or
retitled on the site are missing: those keys are skipped and counted. docs/index_term_patterns.py says how
the data was drafted.

    python manage.py load_index_terms
"""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from berkeley.models import IndexTerm, PossibleIndexTerm

from ._index_terms import POSSIBLE, TERMS
from .load_keywords import find


def found(keys, missing):
    """The entries the keys name, adding the keys that name none to
    missing."""
    pubs = []
    for key in keys:
        try:
            pubs.append(find(key))
        except CommandError:
            missing.add(key)
    return pubs


class Command(BaseCommand):
    help = "Fill the index from _index_terms.py (idempotent)."

    @transaction.atomic
    def handle(self, *args, **options):
        terms = links = 0
        missing = set()
        for name, keys in TERMS.items():
            term, is_new = IndexTerm.objects.get_or_create(name=name)
            terms += is_new
            have = set(term.entries.values_list("id", flat=True))
            new = [p for p in found(keys, missing) if p.id not in have]
            term.entries.add(*new)
            links += len(new)

        doubts = 0
        for name, (details, keys) in POSSIBLE.items():
            doubt, is_new = PossibleIndexTerm.objects.get_or_create(
                name=name, defaults={"details": details})
            doubts += is_new
            have = set(doubt.entries.values_list("id", flat=True))
            doubt.entries.add(*[p for p in found(keys, missing)
                                if p.id not in have])

        self.stdout.write(f"Added {terms} index terms, {links} links and "
                          f"{doubts} possible index terms.")
        if missing:
            self.stdout.write(f"{len(missing)} entries were not found: "
                              + "; ".join(sorted(
                                  repr(k[:1] + k[2:]) for k in missing)[:5])
                              + ("; ..." if len(missing) > 5 else ""))
