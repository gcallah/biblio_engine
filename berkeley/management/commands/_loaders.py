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


def get_publisher(name, publishers, city=None):
    """publishers maps a name to its usual (city, province); city
    overrides the usual one. The same press in another city is stored as
    its own Publisher, since citations take the place from its address.
    A blank city is stored as ""."""
    default_city, province = publishers.get(name, ("", ""))
    city = city or default_city or ""
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


def set_subject(pub, name):
    """Give pub the named subject; returns True if it changed."""
    from berkeley.models import Subject
    subject, _ = Subject.objects.get_or_create(name=name)
    if pub.subject_id == subject.id:
        return False
    pub.subject = subject
    pub.save(update_fields=["subject"])
    return True


def get_host(key, data, book_type):
    """The book a chapter is in: an existing book of book_type (key is
    its title) or a data.HOSTS entry, stored as Works Mentioning."""
    from django.core.management.base import CommandError
    from berkeley.models import Publication
    if key not in data.HOSTS:
        try:
            return Publication.objects.get(title=key, pub_type=book_type)
        except Publication.DoesNotExist:
            raise CommandError(f"Book not in the database: {key!r}. "
                               "Run the book loaders first.")
    book = data.HOSTS[key]
    publisher = (get_publisher(book["publisher"], data.PUBLISHERS,
                               book.get("city"))
                 if book.get("publisher") else None)
    host, is_new = Publication.objects.get_or_create(
        title=book["title"], year=book["year"], pub_type="MENT",
        defaults={"publisher": publisher,
                  "city": "" if publisher else book.get("city", "")})
    if is_new:
        add_people(host, book)
    set_subject(host, book["subject"])
    return host


SHORT_FIELDS = ("volume", "issue", "day", "month", "pages", "url", "doi")


def load_short_works(data, pub_type, book_type):
    """Load data.ARTICLES (in a journal) and data.CHAPTERS (in a
    book) as pub_type entries.
    Works are matched on title, year and journal or book. Subjects,
    URL/DOI and "reviews_book" are applied on every run. A work with
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
        pub, is_new = Publication.objects.get_or_create(
            title=item["title"], year=year, pub_type=pub_type, **key,
            defaults=fields)
        changed = set_subject(pub, item["subject"])
        links = {f: fields[f] for f in ("url", "doi") if fields[f]}
        if any(getattr(pub, f) != v for f, v in links.items()):
            for f, v in links.items():
                setattr(pub, f, v)
            pub.save(update_fields=list(links))
            changed = True
        book = (Publication.objects.filter(
            title=item["reviews_book"], pub_type__in=BOOK_TYPES).first()
            if item.get("reviews_book") else None)
        if book:  # linked once the book is loaded (load_data.sh order)
            if pub.pub_reviewed_id != book.id:
                pub.pub_reviewed = book
                pub.save(update_fields=["pub_reviewed"])
                changed = True
        if is_new:
            created += 1
            add_people(pub, item)
        elif changed:
            updated += 1
    return created, updated, len(works)

