from django.db import models

# Create your models here.

class Person(models.Model):
    fname = models.CharField(max_length=64, default="")
    mname = models.CharField(max_length=64, default="", blank=True)
    lname = models.CharField(max_length=64)
    descr = models.CharField(max_length=512, default="", blank=True)
    yob = models.CharField(max_length=4, default="", blank=True)
    yod = models.CharField(max_length=4, default="", blank=True)

    def __str__(self):
        return self.fname + " " + self.lname


class Publisher(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=128, default="")
    province = models.CharField(max_length=128, default="", blank=True)
    country = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=512)
    publisher = models.ForeignKey(Publisher)
    year = models.CharField(max_length=4)
    edition = models.CharField(max_length=4, default="", blank=True)
    prim_author = models.ForeignKey(Person, related_name='prim_author', default="")
    editor = models.ForeignKey(Person, default="", related_name="editor", blank=True,
            null=True)
    translator = models.ForeignKey(Person, default="", related_name="translator",
            blank=True, null=True)
    city = models.CharField(max_length=128, default="", blank=True)
    isbn = models.CharField(max_length=24, default="")  # 24 to account for future ISBN expansion
    language = models.CharField(max_length=32, default="", blank=True)
    descr = models.CharField(max_length=512, default="", blank=True)

    def __str__(self):
        return self.title

