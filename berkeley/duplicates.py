"""Possible duplicates, for the editors' to-do page, and merging two
records into one.

A duplicate creeps in now and then: a person added again under initials,
an entry saved twice, a publisher typed in anew. The to-do page lists
pairs that look alike; an editor either merges them (everything that
pointed to the one dropped then points to the one kept) or marks them
not the same (NotDuplicate), and either way the pair leaves the list."""
import re
from itertools import combinations

from django.db import transaction

from .models import NotDuplicate, Person, Publication, Publisher, UNKNOWN_ID

KINDS = {"person": Person, "publication": Publication,
         "publisher": Publisher}


def _plain(text):
    """Without case, punctuation or spacing, '&' read as 'and'."""
    return re.sub(r"[\W_]+", "", (text or "").replace("&", "and")).lower()


def _given_matches(a, b):
    """'B.' and 'Bhikhu' may be one name; 'Bhikhu' and 'Brian' are not."""
    a, b = _plain(a), _plain(b)
    if not a or not b:
        return True
    if len(a) == 1 or len(b) == 1:
        return a[0] == b[0]
    return a == b


def _initials(names):
    return [n[0] for n in re.findall(r"[^\s.\-]+", (names or "").lower())]


def same_person(a, b):
    """The same last name, and given names that could be the same
    (initials match, no middle initials in conflict)."""
    if _plain(a.lname) != _plain(b.lname):
        return False
    if not _given_matches(a.fname, b.fname):
        return False
    if a.mname and b.mname and _initials(a.mname) != _initials(b.mname):
        return False
    return True


def same_entry(a, b):
    """Same title and year (the grouping), in the same journal or book,
    and by the same authors (or one with none given): many obituaries
    and reviews share a title."""
    if (a.journal_id, a.collection_id) != (b.journal_id, b.collection_id):
        return False
    # by surname: the two may name one author as two people ("B. Parekh"
    # and "Bhikhu Parekh"), which is how a duplicate entry often begins
    mine, theirs = ({_plain(p.lname) for p in x.ordered_authors()}
                    for x in (a, b))
    return not mine or not theirs or mine == theirs


def _pairs(groups, alike=lambda a, b: True):
    for group in groups.values():
        for a, b in combinations(sorted(group, key=lambda o: o.id), 2):
            if alike(a, b):
                yield a, b


def _group(objs, key):
    groups = {}
    for obj in objs:
        k = key(obj)
        if k:
            groups.setdefault(k, []).append(obj)
    return groups


def possible_duplicates():
    """[(kind, label, [(a, b), ...]), ...]: pairs that look like one
    record entered twice, less those marked not the same."""
    dismissed = set(NotDuplicate.objects.values_list(
        "kind", "first_id", "second_id"))
    people = _pairs(_group(Person.objects.all(),
                           lambda p: _plain(p.lname)), same_person)
    pubs = _pairs(_group(
        Publication.objects.prefetch_related("authorship_set__person"),
        lambda p: (_plain(p.title), p.year) if _plain(p.title) else None),
        same_entry)
    presses = _pairs(_group(
        Publisher.objects.select_related("address"),
        lambda p: (_plain(p.name),
                   _plain(p.address.city) if p.address else "")))
    found = []
    for kind, label, pairs in (("person", "People", people),
                               ("publication", "Entries", pubs),
                               ("publisher", "Publishers", presses)):
        pairs = [(a, b) for a, b in pairs
                 if (kind, a.id, b.id) not in dismissed]
        found.append((kind, label, pairs))
    return found


def _is_blank(value):
    return value is None or value == ""


@transaction.atomic
def merge(keep, drop):
    """Merge drop into keep: everything that refers to drop is moved to
    keep (a link keep already has is dropped rather than doubled), keep's
    blank fields are filled from drop's, and drop is deleted."""
    model = type(keep)
    if type(drop) is not model or keep.pk == drop.pk:
        raise ValueError("Merge two different records of one kind.")
    # every foreign key into the model, including the hidden link tables
    # of many-to-many fields (authors, index terms, reprints, ...)
    for rel in model._meta.get_fields(include_hidden=True):
        if not (rel.auto_created and not rel.concrete
                and (rel.one_to_many or rel.one_to_one)):
            continue
        related, field = rel.related_model, rel.field.name
        unique = [u for u in related._meta.unique_together if field in u]
        for row in related._base_manager.filter(**{field: drop}):
            clash = any(related._base_manager.filter(
                **{f: (keep if f == field else getattr(row, f))
                   for f in u}).exclude(pk=row.pk).exists()
                for u in unique)
            if clash:
                row.delete()
            else:
                setattr(row, field, keep)
                row.save()
    # a record now pointing to itself (a reprint of itself, a chapter of
    # itself) points nowhere
    for rel in model._meta.get_fields(include_hidden=True):
        if (rel.auto_created and not rel.concrete and rel.one_to_many
                and rel.related_model is model):
            model._base_manager.filter(
                pk=keep.pk, **{rel.field.name: keep}).update(
                **{rel.field.name: None})
        elif (rel.auto_created and not rel.concrete and rel.one_to_many
              and rel.related_model._meta.auto_created):
            through = rel.related_model
            links = [f.name for f in through._meta.fields
                     if f.is_relation and f.related_model is model]
            if len(links) == 2:
                through.objects.filter(**{links[0]: keep,
                                          links[1]: keep}).delete()
    keep.refresh_from_db()
    for field in model._meta.concrete_fields:
        if field.primary_key:
            continue
        mine, theirs = (getattr(keep, field.attname),
                        getattr(drop, field.attname))
        if field.attname == "subject_id" and mine == UNKNOWN_ID:
            mine = None
        if _is_blank(mine) and not _is_blank(theirs) and theirs != drop.pk:
            setattr(keep, field.attname, theirs)
    keep.save()
    # deleting drop must take nothing with it (chapters and reviews of a
    # book are deleted with it): stop, undoing all of the above, if
    # anything still refers to it
    for rel in model._meta.get_fields(include_hidden=True):
        if (rel.auto_created and not rel.concrete
                and (rel.one_to_many or rel.one_to_one)
                and rel.related_model._base_manager.filter(
                    **{rel.field.name: drop}).exists()):
            raise RuntimeError(f"{drop} is still referred to by "
                               f"{rel.related_model._meta.verbose_name}.")
    NotDuplicate.objects.filter(kind=model._meta.model_name).filter(
        first_id=drop.pk).delete()
    NotDuplicate.objects.filter(kind=model._meta.model_name).filter(
        second_id=drop.pk).delete()
    drop.delete()
    return keep


def describe(obj):
    """(its name, its page on the site, a note to tell it apart), for
    the to-do page."""
    if isinstance(obj, Person):
        works = (obj.authorship_set.count() + obj.editorship_set.count()
                 + obj.reviewees.count() + obj.translators.count())
        note = ", ".join(n for n in (
            obj.life_years(), obj.affiliation,
            f"{works} entr{'y' if works == 1 else 'ies'}") if n)
        return obj.inverted_name(), obj.get_absolute_url(), note
    if isinstance(obj, Publication):
        authors = ", ".join(a.lname for a in obj.ordered_authors())
        where = obj.journal or obj.collection or obj.publisher or ""
        note = ", ".join(str(n) for n in (
            authors, obj.year, obj.get_pub_type_display(),
            f"in {where}" if where else "") if n)
        return str(obj), obj.get_absolute_url(), note
    works = obj.publication_set.count() + obj.journal_set.count()
    note = ", ".join(n for n in (
        str(obj.address) if obj.address else "",
        f"{works} entr{'y' if works == 1 else 'ies'} or journals") if n)
    return obj.name, obj.get_absolute_url(), note
