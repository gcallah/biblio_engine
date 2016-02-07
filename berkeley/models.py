from django.db import models

# Create your models here.

class SingleNameModel(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class UrlModel(models.Model):
    url = models.CharField(max_length=512, default="", blank=True, null=True)

    class Meta:
        abstract = True


class Institution(SingleNameModel, UrlModel):
    """
    More fields to come.
    """


class Person(models.Model):
    fname = models.CharField(max_length=64, default="")
    mname = models.CharField(max_length=64, default="", blank=True)
    lname = models.CharField(max_length=64)
    descr = models.CharField(max_length=512, default="", blank=True)
    yob = models.CharField(max_length=4, default="", blank=True)
    yod = models.CharField(max_length=4, default="", blank=True)
    url = models.CharField(max_length=512, default="", blank=True, null=True)
    institution = models.ForeignKey(Institution, null=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname


class Publisher(SingleNameModel):
    city = models.CharField(max_length=128, default="")
    province = models.CharField(max_length=128, default="", blank=True)
    country = models.CharField(max_length=128, default="")


class Journal(SingleNameModel):
    publisher = models.ForeignKey(Publisher, blank=True, null=True)


class Publication(models.Model):
    title = models.CharField(max_length=512)
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    journal = models.ForeignKey(Journal, blank=True, null=True)
    year = models.CharField(max_length=4)
    edition = models.CharField(max_length=4, default="", blank=True)
    authors = models.ManyToManyField(Person, related_name="authors")
    editors = models.ManyToManyField(Person,
            related_name="editors", default="",
            blank=True
    )
    translator = models.ManyToManyField(
        Person, default="", related_name="translator",
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
    url = models.CharField(max_length=512, default="", blank=True)

    def __str__(self):
        return self.title

