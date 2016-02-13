from django.db import models


PERSON_NAME_LEN = 64
STREET_NAME_LEN = 64
CITY_NAME_LEN = 64
PROV_NAME_LEN = 32
COUNTRY_NAME_LEN = 64
YEAR_LEN = 4

SUBJECT_CHOICES = (
    ('', ''),
    ('COMP', 'Computer Science'),
    ('ECON', 'Economics'),
    ('EDIT', 'Editorial'),
    ('HIST', 'History'),
    ('PHIL', 'Philosophy'),
    ('POLI', 'Politics'),
)


class SingleNameModel(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class SubjectModel(models.Model):
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=4,
            blank=True, null=True, default="")

    class Meta:
        abstract = True


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


class Institution(SingleNameModel, UrlModel, DescrModel):
    address = models.ForeignKey(Address, null=True, blank=True)


class Person(UrlModel, DescrModel):
    fname = models.CharField(max_length=PERSON_NAME_LEN, default="")
    mname = models.CharField(max_length=PERSON_NAME_LEN, default="", blank=True)
    lname = models.CharField(max_length=PERSON_NAME_LEN)
    yob = models.IntegerField(blank=True, null=True)
    yod = models.IntegerField(blank=True, null=True)
    institution = models.ForeignKey(Institution, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname


class Publisher(SingleNameModel, UrlModel, DescrModel):
    address = models.ForeignKey(Address, null=True, blank=True)


class Journal(SingleNameModel, UrlModel, DescrModel, SubjectModel):
    publisher = models.ForeignKey(Publisher, blank=True, null=True)


class Collection(SingleNameModel, UrlModel, DescrModel):
    publisher = models.ForeignKey(Publisher, blank=True, null=True)


class Publication(UrlModel, SubjectModel):
    title = models.CharField(max_length=512)
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    journal = models.ForeignKey(Journal, blank=True, null=True)
    collection = models.ForeignKey(Collection, blank=True, null=True)
    year = models.IntegerField()
    pages = models.CharField(max_length=12, default="", blank=True)
    edition = models.CharField(max_length=4, default="", blank=True)
    authors = models.ManyToManyField(Person, related_name="authors",
            blank=True
    )
    editors = models.ManyToManyField(Person,
            related_name="editors", default="",
            blank=True
    )
    translators = models.ManyToManyField(
        Person, default="", related_name="translators",
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

    def __str__(self):
        return self.title

