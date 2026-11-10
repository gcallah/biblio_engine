"""The Django admin, which is where logged-in editors edit the
bibliography: the edit pencils on the site link to these pages. Logins are
made with manage.py add_editor; every editor can edit everything."""
from django import forms
from django.contrib import admin

from .models import Address
from .models import Authorship
from .models import Editorship
from .models import AdminEmail
from .models import Institution
from .models import Journal
from .models import Keyword
from .models import Person
from .models import Publication
from .models import Publisher
from .models import Site
from .models import Subject

admin.site.site_header = "Michael Oakeshott Bibliography: editing"
admin.site.site_title = "Oakeshott Bibliography editing"
admin.site.index_title = "Records"
admin.site.site_url = "/oakeshott/"

admin.site.register(Address)
admin.site.register(AdminEmail)
admin.site.register(Institution)
admin.site.register(Site)
admin.site.register(Subject)


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("lname", "fname", "mname", "yob", "yod", "affiliation")
    search_fields = ("lname", "fname")


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ("name", "publisher")
    search_fields = ("name",)
    autocomplete_fields = ("publisher",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name",)


class AuthorshipInline(admin.TabularInline):
    model = Authorship
    fields = ('person', 'position')
    autocomplete_fields = ('person',)
    extra = 1


class EditorshipInline(admin.TabularInline):
    model = Editorship
    fields = ('person', 'position')
    autocomplete_fields = ('person',)
    extra = 1


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        # authors and editors are edited in the ordered inlines below; the
        # plain many-to-many boxes would add people with no position
        exclude = ("authors", "editors")
        widgets = {"abstract": forms.Textarea(attrs={"rows": 8,
                                                     "cols": 80})}


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    form = PublicationForm
    inlines = [AuthorshipInline, EditorshipInline]
    list_display = ("__str__", "year", "pub_type", "subject")
    list_filter = ("pub_type", "subject")
    search_fields = ("title", "authors__lname", "journal__name")
    autocomplete_fields = ("publisher", "journal", "collection",
                           "pub_reviewed", "translators", "reviewees",
                           "reprinted_in", "keywords")
