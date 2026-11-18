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
