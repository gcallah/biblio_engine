"""Helpers shared by the data loaders (the leading underscore keeps
Django from treating this module as a management command)."""
import re

from berkeley.models import Address, Person, Publisher


def get_person(name):
    """name is (first, middle, last); people are matched on first and
    last name."""
    fname, mname, lname = name
    person, _ = Person.objects.get_or_create(
        fname=fname, lname=lname, defaults={"mname": mname})
    return person


def _initials(names):
    """'John' -> 'J', 'A. J.' -> 'AJ', 'J.-P.' -> 'JP'."""
    return "".join(w[0] for w in re.split(r"[\s.\-]+", names or "") if w)


def get_reviewer(name):
    """An existing person with this last name and first initial, and no
    conflicting middle initials ("W. J." matches Wendell John), else a
    new one. Lets a source that gives only initials reuse a person who is
    already in the database under a full name."""
    fname, mname, lname = name
    for person in Person.objects.filter(lname=lname):
        if person.fname[:1] != fname[:1]:
            continue
        if mname and person.mname and \
                _initials(mname) != _initials(person.mname):
            continue
        return person
    return get_person(name)


def get_publisher(name, publishers, city=None, province=None):
    """publishers maps a name to its usual (city, province); city
    overrides the usual one, and then province is the one given (the
    usual province belongs to the usual city). The same press in another
    city is stored as its own Publisher, since citations take the place
    from its address. A blank city is stored as ""."""
    default_city, default_province = publishers.get(name, ("", ""))
    if city and city != default_city:
        province = province or ""
    else:
        city, province = default_city or "", default_province
    publisher = Publisher.objects.filter(name=name,
                                         address__city=city).first()
    if publisher is None:
        address = Address.objects.create(city=city, province=province)
        publisher = Publisher.objects.create(name=name, address=address)
    return publisher


def add_people(pub, item):
    """Attach item's authors and editors to pub, in title-page order."""
    from berkeley.models import Authorship, Editorship
    for pos, name in enumerate(item.get("authors", []), 1):
        Authorship.objects.create(publication=pub, person=get_person(name),
                                  position=pos)
    for pos, name in enumerate(item.get("editors", []), 1):
        Editorship.objects.create(publication=pub, person=get_person(name),
                                  position=pos)


def is_blank(obj, field):
    """A field the loaders may fill: empty, or (for a subject) still the
    default "Uncategorized"."""
    from berkeley.models import UNKNOWN_ID
    if field in ("subject", "subject_id"):
        return getattr(obj, "subject_id") in (None, UNKNOWN_ID)
    return getattr(obj, field) in (None, "")


def fill_blanks(obj, values):
    """Set the fields in values that are blank on obj (is_blank) and save
    them. The live database is the master copy and editors change it on
    the site, so the loaders never overwrite a field that has a value.
    Returns the fields that were set."""
    changed = [f for f, v in values.items()
               if v not in (None, "") and is_blank(obj, f)
               and getattr(obj, f) != v]
    for f in changed:
        setattr(obj, f, values[f])
    if changed:
        obj.save(update_fields=changed)
    return changed


def add_missing(manager, objs):
    """Link objs through a many-to-many manager without unlinking anything
    (an editor may have added links). Returns True if any were added."""
    missing = [o for o in objs if o not in set(manager.all())]
    if missing:
        manager.add(*missing)
    return bool(missing)


def set_subject(pub, name):
    """Give pub the named subject, unless an editor has already given it
    one (see fill_blanks); returns True if it changed."""
    from berkeley.models import Subject
    subject, _ = Subject.objects.get_or_create(name=name)
    if pub.subject_id == subject.id or not is_blank(pub, "subject"):
        return False
    pub.subject = subject
    pub.save(update_fields=["subject"])
    return True


def make_book(book, data, pub_type):
    """Store book (a dict: title, year, subject, publisher or city,
    authors, editors, url, doi) as a pub_type entry, matched on title
    and year."""
    publisher = (get_publisher(book["publisher"], data.PUBLISHERS,
                               book.get("city"), book.get("province"))
                 if book.get("publisher") else None)
    from berkeley.models import Publication
    pub, is_new = Publication.objects.get_or_create(
        title=book["title"], year=book["year"], pub_type=pub_type,
        defaults={"publisher": publisher,
                  "city": "" if publisher else book.get("city", ""),
                  "url": book.get("url", ""), "doi": book.get("doi", "")})
    if is_new:
        add_people(pub, book)
    changed = set_subject(pub, book["subject"])
    return pub, is_new, changed


def get_host(key, data, book_type):
    """The book a chapter is in: an existing book of book_type (a type,
    or a tuple of types; key is its title) or a data.HOSTS entry, stored
    as Works Mentioning."""
    from django.core.management.base import CommandError
    from berkeley.models import Publication
    if key not in data.HOSTS:
        types = (book_type,) if isinstance(book_type, str) else book_type
        try:
            return Publication.objects.get(title=key, pub_type__in=types)
        except Publication.DoesNotExist:
            raise CommandError(f"Book not in the database: {key!r}. "
                               "Run the book loaders first.")
    return make_book(data.HOSTS[key], data, "MENT")[0]


def same_people(pub, item):
    """True if pub's authors are item's authors (first and last names)."""
    have = {(p.fname, p.lname) for p in pub.ordered_authors()}
    return have == {(f, l) for f, _, l in item.get("authors", [])}


SHORT_FIELDS = ("volume", "issue", "day", "month", "pages", "url", "doi")


def load_short_works(data, pub_type, book_type):
    """Load data.ARTICLES (in a journal) and data.CHAPTERS (in a
    book) as pub_type entries.
    Works are matched on title, year and journal or book (and on their
    authors too, if "match_authors" is set). book_type is the type, or
    tuple of types, of an existing host book. Subjects,
    URL/DOI and "reviews_book" fill blank fields on every run (they
    never overwrite an editor's change; see fill_blanks). A work with
    "reviews_book" (the title of a book by or about Oakeshott) is a
    review essay: it stays a short work but links to the book it
    reviews. Returns (created, updated, total)."""
    from berkeley.models import BOOK_TYPES, Journal, Publication
    created = updated = 0
    works = ([(item, "journal") for item in data.ARTICLES] +
             [(item, "chapter") for item in data.CHAPTERS])
    for item, kind in works:
        fields = {f: item.get(f, "") for f in SHORT_FIELDS}
        if kind == "journal":
            journal, _ = Journal.objects.get_or_create(name=item["journal"])
            key = {"journal": journal}
            year = item["year"]
        else:
            host = get_host(item["book"], data, book_type)
            key = {"collection": host}
            year = item.get("year", host.year)
        if item.get("match_authors"):
            # Several pieces with one title in one place (e.g. the
            # obituaries in one newspaper): told apart by their authors.
            pub = next((p for p in Publication.objects.filter(
                title=item["title"], year=year, pub_type=pub_type, **key)
                if same_people(p, item)), None)
            is_new = pub is None
            if is_new:
                pub = Publication.objects.create(
                    title=item["title"], year=year, pub_type=pub_type,
                    **key, **fields)
        else:
            pub, is_new = Publication.objects.get_or_create(
                title=item["title"], year=year, pub_type=pub_type, **key,
                defaults=fields)
        changed = set_subject(pub, item["subject"])
        if fill_blanks(pub, {f: fields[f] for f in ("url", "doi")}):
            changed = True
        book = (Publication.objects.filter(
            title=item["reviews_book"], pub_type__in=BOOK_TYPES).first()
            if item.get("reviews_book") else None)
        if book:  # linked once the book is loaded (load_data.sh order)
            if pub.pub_reviewed_id is None:
                pub.pub_reviewed = book
                pub.save(update_fields=["pub_reviewed"])
                changed = True
        if is_new:
            created += 1
            add_people(pub, item)
        elif changed:
            updated += 1
    return created, updated, len(works)

