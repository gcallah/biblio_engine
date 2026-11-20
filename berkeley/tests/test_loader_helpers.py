"""Helpers shared by every site's data loaders."""
from django.test import TestCase


class GetPublisherTest(TestCase):
    """A press in other than its usual city doesn't take the usual
    city's province."""

    def test_other_city_takes_given_province(self):
        from berkeley.management.commands._loaders import get_publisher
        presses = {"Palgrave Macmillan": ("Cham", "Switzerland")}
        usual = get_publisher("Palgrave Macmillan", presses)
        other = get_publisher("Palgrave Macmillan", presses, "New York",
                              "NY")
        bare = get_publisher("Palgrave Macmillan", presses, "Boston")
        self.assertEqual((usual.address.city, usual.address.province),
                         ("Cham", "Switzerland"))
        self.assertEqual((other.address.city, other.address.province),
                         ("New York", "NY"))
        self.assertEqual(bare.address.province, "")


class ApplyAbstractsTest(TestCase):
    """Abstracts fill blanks only, on exactly one entry unless the key
    names one review of several books."""

    def setUp(self):
        from berkeley.models import Journal, Publication, Subject, UNKNOWN_ID
        Subject.objects.get_or_create(id=UNKNOWN_ID,
                                      defaults={"name": "Uncategorized"})
        journal = Journal.objects.create(name="Weekly")
        self.pubs = [Publication.objects.create(
            title="Two Books", year=2008, journal=journal, pub_type="RVAB",
            review=book) for book in ("First", "Second")]
        self.one = Publication.objects.create(
            title="One Essay", year=2008, journal=journal, pub_type="SWAB",
            abstract="Written by an editor.")

    def apply(self, data):
        from berkeley.management.commands._loaders import apply_abstracts
        return apply_abstracts(data)

    def test_several_matches_need_same_piece(self):
        from django.core.management.base import CommandError
        key = ("Two Books", 2008, "Weekly")
        with self.assertRaises(CommandError):
            self.apply({key: {"abstract": "A review."}})
        self.assertEqual(self.apply({key: {"abstract": "A review.",
                                           "same_piece": True}}), 2)
        for pub in self.pubs:
            pub.refresh_from_db()
            self.assertEqual(pub.abstract, "A review.")

    def test_keeps_an_editors_abstract(self):
        self.assertEqual(self.apply({("One Essay", 2008, "Weekly"):
                                     {"abstract": "Loaded."}}), 0)
        self.one.refresh_from_db()
        self.assertEqual(self.one.abstract, "Written by an editor.")
