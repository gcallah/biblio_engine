"""Model methods, string forms and integrity rules."""
from django.db import IntegrityError, transaction

from berkeley.models import (
    Address, AdminEmail, Authorship, Journal, Keyword, Person, Publication, Publisher,
    Site, Subject, REVIEW_TYPES, TYPE_CHOICES,
)

from .helpers import BiblioTestCase


class TypeChoicesTest(BiblioTestCase):
    def test_codes_fit_the_column(self):
        max_len = Publication._meta.get_field("pub_type").max_length
        for code, _ in TYPE_CHOICES:
            self.assertLessEqual(len(code), max_len, code)

    def test_codes_are_unique(self):
        codes = [code for code, _ in TYPE_CHOICES]
        self.assertEqual(len(codes), len(set(codes)))

    def test_review_types_are_valid_choices(self):
        codes = {code for code, _ in TYPE_CHOICES}
        self.assertTrue(set(REVIEW_TYPES) <= codes)


class StrTest(BiblioTestCase):
    def test_simple_models(self):
        self.assertEqual(str(Keyword.objects.create(name="liberty")), "liberty")
        self.assertEqual(str(Subject.objects.create(name="Politics")), "Politics")
        self.assertEqual(str(Journal.objects.create(name="Mind")), "Mind")
        self.assertEqual(str(Publisher.objects.create(name="Methuen")), "Methuen")
        self.assertEqual(str(Site.objects.create(name="biblio")), "biblio")
        self.assertEqual(str(AdminEmail.objects.create(email_addr="a@b.org")),
                         "a@b.org")

    def test_person(self):
        self.assertEqual(str(self.person("Michael", "Oakeshott")),
                         "Michael Oakeshott")

    def test_publication_with_title(self):
        self.assertEqual(str(self.pub("Experience and its Modes")),
                         "Experience and its Modes")

    def test_untitled_review(self):
        book = self.pub("On Human Conduct")
        review = self.pub("", pub_type="RVBY", pub_reviewed=book)
        self.assertEqual(str(review), "A Review of On Human Conduct")

    def test_untitled_non_review_is_empty_string(self):
        self.assertEqual(str(self.pub("", pub_type="BKBY")), "")

    def test_authorship(self):
        mo = self.person("Michael", "Oakeshott")
        pub = self.pub("Notebooks", authors=[mo])
        self.assertEqual(str(pub.authorship_set.get()),
                         "1: Michael Oakeshott - Notebooks")


class ReviewHelpersTest(BiblioTestCase):
    def test_review_title_without_reviewed_book(self):
        self.assertEqual(self.pub("").review_title(), "A Review of ")

    def test_reviewed_authors(self):
        book = self.pub("Book", authors=[self.person("Michael", "Oakeshott")])
        review = self.pub("", pub_type="RVAB", pub_reviewed=book)
        self.assertEqual(review.reviewed_authors(), "Michael Oakeshott")
        Authorship.objects.create(publication=book, position=2,
                                  person=self.person("A", "B"))
        self.assertEqual(review.reviewed_authors(), "Michael Oakeshott and A B")
        Authorship.objects.create(publication=book, position=3,
                                  person=self.person("C", "D"))
        self.assertEqual(review.reviewed_authors(),
                         "Michael Oakeshott, A B and C D")

    def test_apa_reviewed_authors(self):
        book = self.pub("Book", authors=[self.person("Michael", "Oakeshott"),
                                         self.person("Isaiah", "Berlin")])
        review = self.pub("", pub_type="RVAB", pub_reviewed=book)
        self.assertEqual(review.apa_reviewed_authors(),
                         "M. Oakeshott and I. Berlin")

    def test_reviewed_authors_without_reviewed_book(self):
        self.assertEqual(self.pub("").reviewed_authors(), "")
        self.assertEqual(self.pub("").apa_reviewed_authors(), "")


class AuthorOrderTest(BiblioTestCase):
    def setUp(self):
        super().setUp()
        self.zed = self.person("Zed", "Zulu")
        self.amy = self.person("Amy", "Alpha")
        self.max = self.person("Max", "Mike")
        self.pub_ = self.pub("Joint Work")

    def test_add_keeps_insertion_order(self):
        self.pub_.authors.add(self.zed)
        self.pub_.authors.add(self.amy)
        self.assertEqual(self.pub_.ordered_authors(), [self.zed, self.amy])

    def test_position_sets_title_page_order(self):
        for person, pos in ((self.zed, 3), (self.amy, 1), (self.max, 2)):
            Authorship.objects.create(publication=self.pub_, person=person,
                                      position=pos)
        self.assertEqual(self.pub_.ordered_authors(),
                         [self.amy, self.max, self.zed])

    def test_reordering(self):
        self.pub_.authors.add(self.zed, self.amy)
        Authorship.objects.filter(person=self.amy).update(position=1)
        Authorship.objects.filter(person=self.zed).update(position=2)
        self.assertEqual(self.pub_.ordered_authors(), [self.amy, self.zed])

    def test_order_is_per_publication(self):
        other = self.pub("Other")
        Authorship.objects.create(publication=self.pub_, person=self.zed, position=1)
        Authorship.objects.create(publication=self.pub_, person=self.amy, position=2)
        Authorship.objects.create(publication=other, person=self.amy, position=1)
        Authorship.objects.create(publication=other, person=self.zed, position=2)
        self.assertEqual(self.pub_.ordered_authors(), [self.zed, self.amy])
        self.assertEqual(other.ordered_authors(), [self.amy, self.zed])

    def test_same_author_cannot_be_added_twice(self):
        Authorship.objects.create(publication=self.pub_, person=self.zed)
        with self.assertRaises(IntegrityError), transaction.atomic():
            Authorship.objects.create(publication=self.pub_, person=self.zed,
                                      position=2)

    def test_deleting_publication_removes_its_authorships(self):
        self.pub_.authors.add(self.zed)
        self.pub_.delete()
        self.assertFalse(Authorship.objects.exists())
        self.assertTrue(Person.objects.filter(pk=self.zed.pk).exists())

    def test_deleting_person_removes_their_authorships(self):
        self.pub_.authors.add(self.zed, self.amy)
        self.zed.delete()
        self.assertEqual(self.pub_.ordered_authors(), [self.amy])

    def test_reverse_lookup_from_person(self):
        self.pub_.authors.add(self.zed)
        self.assertEqual(list(self.zed.authors.all()), [self.pub_])


class AddressStrTest(BiblioTestCase):
    def test_full_address(self):
        a = Address.objects.create(street="Houghton St", city="London",
                                   country="UK")
        self.assertEqual(str(a), "Houghton St, London, UK")

    def test_missing_parts_are_skipped(self):
        self.assertEqual(str(Address.objects.create(city="London")), "London")
        a = Address.objects.create(street=None, city=None, country="UK")
        self.assertEqual(str(a), "UK")
        self.assertEqual(str(Address.objects.create(street=None, city=None,
                                                    country=None)), "")


class PersonNameTest(BiblioTestCase):
    def test_without_middle_name(self):
        p = self.person("Michael", "Oakeshott")
        self.assertEqual(p.natural_name(), "Michael Oakeshott")
        self.assertEqual(p.inverted_name(), "Oakeshott, Michael")
        self.assertEqual(str(p), "Michael Oakeshott")

    def test_with_middle_name(self):
        p = self.person("Michael", "Oakeshott", mname="Joseph")
        self.assertEqual(p.natural_name(), "Michael Joseph Oakeshott")
        self.assertEqual(p.inverted_name(), "Oakeshott, Michael Joseph")

    def test_surname_only(self):
        p = self.person("", "Anonymous")
        self.assertEqual(p.natural_name(), "Anonymous")
        self.assertEqual(p.inverted_name(), "Anonymous")
        self.assertEqual(p.initials(), "")
        self.assertEqual(p.apa_name(), "Anonymous")
        self.assertEqual(p.apa_natural_name(), "Anonymous")

    def test_initials(self):
        p = self.person("Michael", "Oakeshott", mname="Joseph")
        self.assertEqual(p.initials(), "M. J.")
        self.assertEqual(p.apa_name(), "Oakeshott, M. J.")
        self.assertEqual(p.apa_natural_name(), "M. J. Oakeshott")

    def test_initials_of_hyphenated_and_already_initialled_names(self):
        self.assertEqual(self.person("Jean-Paul", "Sartre").initials(), "J.-P.")
        self.assertEqual(self.person("J.", "Smith").initials(), "J.")
        self.assertEqual(self.person("T. S.", "Eliot").initials(), "T. S.")
        self.assertEqual(self.person("Mary Anne", "Evans").initials(), "M. A.")


class CitationAuthorListTest(BiblioTestCase):
    """Author lists for the three citation styles."""

    def with_authors(self, n):
        names = [("Amy", "Alpha"), ("Ben", "Bravo"), ("Cal", "Charlie"),
                 ("Dee", "Delta"), ("Eve", "Echo"), ("Fay", "Foxtrot"),
                 ("Gus", "Golf"), ("Hal", "Hotel"), ("Ida", "India"),
                 ("Jo", "Juliet"), ("Kit", "Kilo")]
        return self.pub("P", authors=[self.person(f, l) for f, l in names[:n]])

    def test_no_authors(self):
        pub = self.with_authors(0)
        self.assertEqual(pub.apa_authors(), "")
        self.assertEqual(pub.mla_authors(), "")
        self.assertEqual(pub.chicago_authors(), "")

    def test_one_author(self):
        pub = self.with_authors(1)
        self.assertEqual(pub.apa_authors(), "Alpha, A.")
        self.assertEqual(pub.mla_authors(), "Alpha, Amy.")
        self.assertEqual(pub.chicago_authors(), "Alpha, Amy.")

    def test_two_authors(self):
        pub = self.with_authors(2)
        self.assertEqual(pub.apa_authors(), "Alpha, A., & Bravo, B.")
        self.assertEqual(pub.mla_authors(), "Alpha, Amy, and Ben Bravo.")
        self.assertEqual(pub.chicago_authors(), "Alpha, Amy, and Ben Bravo.")

    def test_three_authors(self):
        pub = self.with_authors(3)
        self.assertEqual(pub.apa_authors(), "Alpha, A., Bravo, B., & Charlie, C.")
        self.assertEqual(pub.mla_authors(), "Alpha, Amy, et al.")
        self.assertEqual(pub.chicago_authors(),
                         "Alpha, Amy, Ben Bravo, and Cal Charlie.")

    def test_many_authors_et_al_appears_once(self):
        pub = self.with_authors(5)
        self.assertEqual(pub.mla_authors(), "Alpha, Amy, et al.")
        self.assertEqual(pub.chicago_authors(),
                         "Alpha, Amy, Ben Bravo, Cal Charlie, Dee Delta, "
                         "and Eve Echo.")

    def test_chicago_more_than_ten(self):
        pub = self.with_authors(11)
        self.assertEqual(pub.chicago_authors(),
                         "Alpha, Amy, Ben Bravo, Cal Charlie, Dee Delta, "
                         "Eve Echo, Fay Foxtrot, Gus Golf, et al.")
        self.assertEqual(self.with_authors(10).chicago_authors().count("et al"), 0)

    def test_middle_names(self):
        pub = self.pub("P", authors=[
            self.person("Michael", "Oakeshott", mname="Joseph"),
            self.person("Isaiah", "Berlin")])
        self.assertEqual(pub.mla_authors(),
                         "Oakeshott, Michael Joseph, and Isaiah Berlin.")
        self.assertEqual(pub.apa_authors(), "Oakeshott, M. J., & Berlin, I.")

    def test_no_double_full_stop(self):
        pub = self.pub("P", authors=[self.person("J.", "Smith")])
        self.assertEqual(pub.apa_authors(), "Smith, J.")

    def test_title_page_order(self):
        zed, amy = self.person("Zed", "Zulu"), self.person("Amy", "Alpha")
        pub = self.pub("P", authors=[zed, amy])
        self.assertEqual(pub.apa_authors(), "Zulu, Z., & Alpha, A.")
