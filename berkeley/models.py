from django.db import models


HEADER_LEN = 128
PUB_TITLE_LEN = 512
PERSON_NAME_LEN = 64
RANK_LEN = 64
DEPT_LEN = 64
CAMPUS_LEN = 64
STREET_NAME_LEN = 64
CITY_NAME_LEN = 64
DOI_LEN = 64
PROV_NAME_LEN = 32
COUNTRY_NAME_LEN = 64
YEAR_LEN = 4
CODE_LEN = 4
EMAIL_LEN = 80
AFFILIATION_LEN = 128

UNKNOWN_ID = 9

TYPE_CHOICES = (
    ('', ''),
    ('BKBY', 'Books by Oakeshott'),
    ('SWBY', 'Short Works by Oakeshott'),
    ('BKAB', 'Books About Oakeshott'),
    ('SWAB', 'Short Works About Oakeshott'),
    ('MENT', 'Works Mentioning Oakeshott'),
    ('RVBY', 'Book Reviews by Oakeshott'),
    ('RVAB', 'Book Reviews of Books About Oakeshott'),
)

REVIEW_TYPES = ('RVBY', 'RVAB')
BOOK_TYPES = ('BKBY', 'BKAB')
SHORT_TYPES = ('SWBY', 'SWAB')

CATEGORIES = (
    ('', ''),
    ('SOCDIST', 'Social Distancing'),
    ('MONTRG', 'Monitoring / Situational Awareness Strategies & Data'),
    ('POLSOR', 'PPE & Other Essential Supplies & Services – Policies & Sourcing'),
    ('MED', 'Medical / Public Health Guidance for Individuals & Organizations'),
    ('WORK', 'Sustained Work from Home Strategies'),
    ('HEALTHSTAT', 'Health Status Confirmation Strategies & Technologies'),
    ('COMM', 'Communications (internal & external)'),
    ('CLEANING', 'Cleaning & Disinfection'),
    ('HR', 'HR / Personnel Strategies'),
)


class SingleNameModel(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class UrlModel(models.Model):
    url = models.CharField(max_length=512, default="",
            blank=True, null=True)

    class Meta:
        abstract = True


class DescrModel(models.Model):
    descr = models.CharField(max_length=512, default="", blank=True,
            null=True)

    class Meta:
        abstract = True


class EmailModel(models.Model):
    email_addr = models.CharField(max_length=EMAIL_LEN, default="", blank=True, null=True)

    class Meta:
        abstract = True


class Keyword(SingleNameModel):
    """
    All fields from abstract classes right now.
    """


class Address(models.Model):
    street = models.CharField(max_length=STREET_NAME_LEN, default="",
            null=True, blank=True)
    office = models.CharField(max_length=STREET_NAME_LEN, default="",
            null=True, blank=True)
    city = models.CharField(max_length=CITY_NAME_LEN, default="",
            null=True, blank=True)
    province = models.CharField(max_length=PROV_NAME_LEN, default="",
            null=True, blank=True)
    country = models.CharField(max_length=COUNTRY_NAME_LEN, default="",
            null=True, blank=True)

    def __str__(self):
        parts = (self.street, self.city, self.country)
        return ", ".join(p for p in parts if p)


# this model captures site specific info
class Site(SingleNameModel, UrlModel, DescrModel):
    header = models.CharField(max_length=HEADER_LEN, default="")


class Institution(SingleNameModel, UrlModel, DescrModel):
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE,)


class Person(UrlModel, DescrModel, EmailModel):
    fname = models.CharField(max_length=PERSON_NAME_LEN, default="")
    mname = models.CharField(max_length=PERSON_NAME_LEN,
            blank=True, null=True)
    lname = models.CharField(max_length=PERSON_NAME_LEN)
    yob = models.IntegerField(blank=True, null=True)
    yod = models.IntegerField(blank=True, null=True)
    affiliation = models.CharField(max_length=AFFILIATION_LEN, default="",
            blank=True)
    #institution = models.ForeignKey(Institution, null=True, blank=True, on_delete=models.CASCADE,)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.natural_name()

    def _given(self):
        return " ".join(n for n in (self.fname, self.mname) if n)

    def natural_name(self):
        """'Michael Joseph Oakeshott'"""
        return " ".join(n for n in (self._given(), self.lname) if n)

    def inverted_name(self):
        """'Oakeshott, Michael Joseph'"""
        given = self._given()
        return f"{self.lname}, {given}" if given else self.lname

    def initials(self):
        """'M. J.' for Michael Joseph; hyphenated names keep the hyphen,
        so Jean-Paul becomes 'J.-P.'."""
        def initial(word):
            return '-'.join(part[0] + '.' for part in word.split('-') if part)
        return ' '.join(initial(w) for w in self._given().split())

    def apa_name(self):
        """'Oakeshott, M. J.'"""
        initials = self.initials()
        return f"{self.lname}, {initials}" if initials else self.lname

    def life_years(self):
        """'(1901–1990)', '(b. 1959)', '(d. 1679)', or '' if unknown."""
        if self.yob and self.yod:
            return f"({self.yob}–{self.yod})"
        if self.yob:
            return f"(b. {self.yob})"
        if self.yod:
            return f"(d. {self.yod})"
        return ""

    def has_bio(self):
        """True if there is anything to show in an author popup."""
        return bool(self.descr or self.affiliation or self.yob or self.yod)

    def apa_natural_name(self):
        """'M. J. Oakeshott'"""
        return " ".join(n for n in (self.initials(), self.lname) if n)

    class Meta:
        ordering = ['lname']


class Publisher(SingleNameModel, UrlModel, DescrModel):
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE,)


class Collection(SingleNameModel, UrlModel, DescrModel):
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.CASCADE,)


class Subject(SingleNameModel):
    code = models.CharField(max_length=CODE_LEN, null=True, blank=True)


class Journal(SingleNameModel, UrlModel, DescrModel):
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.CASCADE,)
    subject = models.ForeignKey(Subject, default=UNKNOWN_ID, on_delete=models.CASCADE,)


class Publication(UrlModel):
    title = models.CharField(max_length=PUB_TITLE_LEN,
            blank=True, null=True, default="")
    pub_type = models.CharField(choices=TYPE_CHOICES, max_length=4,
            blank=True, null=True, default="")
    publisher = models.ForeignKey(Publisher, blank=True, null=True,  on_delete=models.CASCADE,)
    subject = models.ForeignKey(Subject, default=UNKNOWN_ID, on_delete=models.CASCADE,)
    journal = models.ForeignKey(Journal, blank=True, null=True, on_delete=models.CASCADE,)
    collection = models.ForeignKey('berkeley.Publication', blank=True,
            null=True, related_name="coll",  on_delete=models.CASCADE,)
    pub_reviewed = models.ForeignKey('berkeley.Publication', blank=True,
            null=True, related_name="pub_rev", on_delete=models.CASCADE,)
    year = models.IntegerField()
    volume = models.CharField(max_length=12, default="", blank=True)
    issue = models.CharField(max_length=12, default="", blank=True)
    month = models.CharField(max_length=10, default="", blank=True)
    day = models.CharField(max_length=10, default="", blank=True)
    pages = models.CharField(max_length=24, default="", blank=True)
    edition = models.CharField(max_length=4, default="", blank=True)
    medium = models.CharField(max_length=12, default="", blank=True)
    authors = models.ManyToManyField(Person, through="Authorship",
            related_name="authors", blank=True)
    editors = models.ManyToManyField(Person, through="Editorship",
            related_name="editors", blank=True)
    translators = models.ManyToManyField(
        Person, default="", related_name="translators",
        blank=True
    )
    reviewees = models.ManyToManyField(
        Person, default="", related_name="reviewees",
        blank=True
    )
    keywords = models.ManyToManyField(
        Keyword, default="", related_name="keywords",
        blank=True
    )
    city = models.CharField(max_length=128, default="", blank=True)
    isbn = models.CharField(max_length=24,
            default="",
            blank=True, null=True
    )  # 24 to account for future ISBN expansion
    sn = models.CharField(max_length=12, default="", blank=True, null=True)
    language = models.CharField(max_length=32, default="", blank=True)
    abstract = models.CharField(max_length=1024, default="", blank=True)
    doi = models.CharField(max_length=DOI_LEN, default="", blank=True)
    # A reviewed book that is not itself in the bibliography: its title,
    # and its authors as written, e.g. "J. Needham (ed.)". The authors
    # are also linked as reviewees, so they can be searched.
    review = models.CharField(max_length=128, default="", blank=True)
    reviewed_names = models.CharField(max_length=128, default="",
                                      blank=True)

    def __str__(self):
        if self.title:
            return self.title
        elif self.pub_type in REVIEW_TYPES:
            return self.review_title()
        return ''

    def ordered_authors(self):
        """Authors in title-page order (Authorship.position). Honours a
        prefetch of 'authorship_set__person'."""
        links = self.authorship_set.all()
        if 'authorship_set' not in getattr(self, '_prefetched_objects_cache',
                                           {}):
            links = links.select_related('person')
        return [a.person for a in links]

    def ordered_editors(self):
        """Editors in title-page order (Editorship.position). Uses
        editorship_set.all() so a prefetch of 'editorship_set__person'
        is honoured."""
        links = self.editorship_set.all()
        if 'editorship_set' not in getattr(self, '_prefetched_objects_cache',
                                           {}):
            links = links.select_related('person')
        return [e.person for e in links]

    @staticmethod
    def _sentence(text):
        """End a citation element with exactly one full stop."""
        if not text:
            return ''
        return text if text.endswith(('.', '?', '!')) else text + '.'

    def title_stop(self):
        """'.' to close the title, or '' when it already ends in '.',
        '?' or '!' (e.g. '... Hegel, et al.')."""
        return '' if (self.title or '').endswith(('.', '?', '!')) else '.'

    def title_sentence(self):
        """The title ending in one full stop (none after '?' or '!')."""
        return self._sentence(self.title)

    def is_book(self):
        """Cited as a book: Books by/about Oakeshott, and Works Mentioning
        Oakeshott that are not in a journal or a book."""
        return self.pub_type in BOOK_TYPES or (
            self.pub_type == 'MENT' and not self.journal_id
            and not self.collection_id)

    def is_chapter(self):
        """A short work that is a part of a book (its collection)."""
        return self.pub_type in SHORT_TYPES and self.collection_id is not None

    def apa_place_publisher(self):
        """'London, England: Methuen'; just the city when there is no
        publisher; '' when neither is known."""
        if not self.publisher:
            return self.city
        addr = self.publisher.address
        place = ', '.join(p for p in (addr.city, addr.province) if p) \
            if addr else ''
        return f"{place}: {self.publisher.name}" if place \
            else self.publisher.name

    def place_publisher(self):
        """MLA / Chicago: 'London: Methuen'."""
        if not self.publisher:
            return self.city
        city = self.publisher.address.city if self.publisher.address else ''
        return f"{city}: {self.publisher.name}" if city \
            else self.publisher.name

    def apa_pages(self):
        """'pp. 2-20', or 'p. 562' for a single page."""
        if not self.pages:
            return ''
        return ('pp. ' if '-' in self.pages or ',' in self.pages
                else 'p. ') + self.pages

    def apa_authors(self):
        """APA 7: 'Last, F. M., Last, F., & Last, F.'"""
        names = [a.apa_name() for a in self.ordered_authors()]
        if len(names) > 1:
            names = [', '.join(names[:-1]) + ', & ' + names[-1]]
        return self._sentence(''.join(names))

    def mla_authors(self):
        """MLA 9: 'Last, First.' / 'Last, First, and First Last.' /
        'Last, First, et al.'"""
        authors = self.ordered_authors()
        if not authors:
            return ''
        first = authors[0].inverted_name()
        if len(authors) == 1:
            return self._sentence(first)
        if len(authors) == 2:
            return self._sentence(f"{first}, and {authors[1].natural_name()}")
        return f"{first}, et al."

    def chicago_authors(self):
        """Chicago 17 bibliography: 'Last, First, First Last, and First
        Last.' Lists up to ten authors; beyond that the first seven and
        'et al.'"""
        authors = self.ordered_authors()
        if not authors:
            return ''
        names = [authors[0].inverted_name()]
        if len(authors) > 10:
            names += [a.natural_name() for a in authors[1:7]]
            return ', '.join(names) + ', et al.'
        names += [a.natural_name() for a in authors[1:]]
        if len(names) == 2:
            return self._sentence(f"{names[0]}, and {names[1]}")
        if len(names) > 2:
            names[-1] = 'and ' + names[-1]
        return self._sentence(', '.join(names))

    @staticmethod
    def _join(names, conj):
        """'A', 'A and B', 'A, B, and C' (conj is 'and' or '&')."""
        if len(names) <= 2:
            return f" {conj} ".join(names)
        return ", ".join(names[:-1]) + f", {conj} " + names[-1]

    def apa_editors(self):
        """APA 7, for after the title: 'T. Nardin & L. O'Sullivan, Eds.'"""
        names = [e.apa_natural_name() for e in self.ordered_editors()]
        if not names:
            return ''
        return self._join(names, '&') + (', Ed.' if len(names) == 1 else ', Eds.')

    def apa_in_editors(self):
        """APA 7, a chapter's book editors: 'C. Abel & T. Fuller (Eds.)'."""
        names = [e.apa_natural_name() for e in self.ordered_editors()]
        if not names:
            return ''
        return self._join(names, '&') + (' (Ed.)' if len(names) == 1
                                         else ' (Eds.)')

    def edited_by_lower(self):
        """MLA 9 / Chicago 17 chapters: 'edited by Corey Abel and
        Timothy Fuller'."""
        names = [e.natural_name() for e in self.ordered_editors()]
        return 'edited by ' + self._join(names, 'and') if names else ''

    def edited_by(self):
        """MLA 9 / Chicago 17: 'Edited by Terry Nardin and Luke O'Sullivan.'"""
        names = [e.natural_name() for e in self.ordered_editors()]
        if not names:
            return ''
        return self._sentence('Edited by ' + self._join(names, 'and'))

    def reviewed_authors(self):
        """Names of the reviewed book's authors, e.g. 'A B, C D and E F'."""
        return self._reviewed_names(Person.natural_name)

    def reviewed_authors_sentence(self):
        """reviewed_authors ending in one full stop ('Spragens, Jr.')."""
        return self._sentence(self.reviewed_authors())

    def apa_reviewed_authors(self):
        """Reviewed book's authors with initials, e.g. 'M. Oakeshott'."""
        return self._reviewed_names(Person.apa_natural_name)

    def _reviewed_names(self, name_of):
        if not self.pub_reviewed:
            return self.reviewed_names
        names = [name_of(p) for p in self.pub_reviewed.ordered_authors()]
        if len(names) <= 1:
            return ''.join(names)
        return ', '.join(names[:-1]) + ' and ' + names[-1]

    def reviewed_title(self):
        """Title of the reviewed book, whether or not it is in the
        bibliography."""
        if self.pub_reviewed:
            return self.pub_reviewed.title
        return self.review

    def review_title(self):
        """'Review of J. Needham (ed.), Science, Religion and Reality'."""
        if self.pub_reviewed:
            return 'A Review of ' + self.pub_reviewed.title
        if self.reviewed_names:
            return f"Review of {self.reviewed_names}, {self.review}"
        return 'Review of ' + self.review if self.review else 'A Review'

    class Meta:
        ordering = ['title']


class Authorship(models.Model):
    """Links an author to a publication, with their title-page position."""
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 1 = first-named author. Ties (e.g. authors.add() with no position)
    # fall back to the order the links were created.
    position = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'berkeley_publication_authors'
        unique_together = [('publication', 'person')]
        ordering = ['position', 'id']

    def __str__(self):
        return f"{self.position}: {self.person} - {self.publication}"


class Editorship(models.Model):
    """Links an editor to a publication, with their title-page position."""
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 1 = first-named editor; ties fall back to the order of creation.
    position = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'berkeley_publication_editors'
        unique_together = [('publication', 'person')]
        ordering = ['position', 'id']

    def __str__(self):
        return f"{self.position}: {self.person} (ed.) - {self.publication}"


class AdminEmail(EmailModel):
    def __str__(self):
        return self.email_addr
