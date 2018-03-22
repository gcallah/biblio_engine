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

UNKNOWN_ID = 9

TYPE_CHOICES = (
    ('', ''),
    ('ARTI', 'Article'),
    ('BLOG', 'Blog post'),
    ('BOOK', 'Book'),
    ('REVW', 'Book review'),
    ('COMM', 'Comment'),
    ('PAPR', 'Paper'),
    ('MOVI', 'Movie'),
    ('WWW', 'Website'),
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
        return self.street + ", " + self.city + ", " + self.country


# this model captures site specific info
class Site(SingleNameModel, UrlModel, DescrModel):
    header = models.CharField(max_length=HEADER_LEN, default="")


class Institution(SingleNameModel, UrlModel, DescrModel):
    address = models.ForeignKey(Address, null=True, blank=True)


class Person(UrlModel, DescrModel, EmailModel):
    fname = models.CharField(max_length=PERSON_NAME_LEN, default="")
    mname = models.CharField(max_length=PERSON_NAME_LEN,
            blank=True, null=True)
    lname = models.CharField(max_length=PERSON_NAME_LEN)
    yob = models.IntegerField(blank=True, null=True)
    yod = models.IntegerField(blank=True, null=True)
    institution = models.ForeignKey(Institution, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname

    class Meta:
        ordering = ['lname']


class Publisher(SingleNameModel, UrlModel, DescrModel):
    address = models.ForeignKey(Address, null=True, blank=True)


class Collection(SingleNameModel, UrlModel, DescrModel):
    publisher = models.ForeignKey(Publisher, blank=True, null=True)


class Subject(SingleNameModel):
    code = models.CharField(max_length=CODE_LEN, null=True, blank=True)


class Journal(SingleNameModel, UrlModel, DescrModel):
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    subject = models.ForeignKey(Subject, default=UNKNOWN_ID)


class Publication(UrlModel):
    title = models.CharField(max_length=PUB_TITLE_LEN,
            blank=True, null=True, default="")
    pub_type = models.CharField(choices=TYPE_CHOICES, max_length=4,
            blank=True, null=True, default="")
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    subject = models.ForeignKey(Subject, default=UNKNOWN_ID)
    journal = models.ForeignKey(Journal, blank=True, null=True)
    collection = models.ForeignKey('berkeley.Publication', blank=True,
            null=True, related_name="coll")
    pub_reviewed = models.ForeignKey('berkeley.Publication', blank=True,
            null=True, related_name="pub_rev")
    year = models.IntegerField()
    volume = models.CharField(max_length=12, default="", blank=True)
    issue = models.CharField(max_length=12, default="", blank=True)
    month = models.CharField(max_length=10, default="", blank=True)
    day = models.CharField(max_length=10, default="", blank=True)
    pages = models.CharField(max_length=12, default="", blank=True)
    edition = models.CharField(max_length=4, default="", blank=True)
    medium = models.CharField(max_length=12, default="", blank=True)
    authors = models.ManyToManyField(Person, related_name="authors", blank=True)
    editors = models.ManyToManyField(Person,
            related_name="editors", default="",
            blank=True
    )
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

    def __str__(self):
        if self.title:
            return self.title
        elif self.pub_type == 'REVW':
            return self.review_title()

    def review_title(self):
        rev_title = 'A Review of '
        if self.pub_reviewed:
            rev_title = rev_title + self.pub_reviewed.title
        return rev_title

    class Meta:
        ordering = ['title']


class AdminEmail(EmailModel):
    def __str__(self):
        return self.email_addr
