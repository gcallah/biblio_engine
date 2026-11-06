"""Helpers shared by the data loaders (the leading underscore keeps
Django from treating this module as a management command)."""
from berkeley.models import Address, Person, Publisher


def get_person(name):
    """name is (first, middle, last); people are matched on first and
    last name."""
    fname, mname, lname = name
    person, _ = Person.objects.get_or_create(
        fname=fname, lname=lname, defaults={"mname": mname})
    return person


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
