"""The Django admin, which is where logged-in editors edit the
bibliography: the edit pencils on the site link to these pages. Logins are
made with manage.py add_editor; every editor can edit everything."""
from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.urls import reverse, reverse_lazy
from django.utils.html import format_html

from .models import Address
from .models import Authorship
from .models import Editorship
from .models import AdminEmail
from .models import Candidate
from .models import IndexTerm
from .models import PossibleIndexTerm
from .models import OpenQuestion
from .models import Institution
from .models import Journal
from .models import Keyword
from .models import Person
from .models import Publication
from .models import Publisher
from .models import Site
from .models import Subject

admin.site.site_header = f"{settings.BIBLIO_SITE['name']} Bibliography: editing"
admin.site.site_title = (f"{settings.BIBLIO_SITE['short_name']} "
                         "Bibliography editing")
admin.site.index_title = "Records"
admin.site.site_url = reverse_lazy("berkeley:search")

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
                           "reprinted_in", "translation_of", "keywords")

    # "Add it" on a possible entry (Candidate) opens this form with
    # ?candidate=<id>: the form starts from a draft read from its citation,
    # and saving links the possible entry to the new one and marks it added.

    def candidate(self, request):
        try:
            return Candidate.objects.get(id=request.GET.get("candidate"))
        except (Candidate.DoesNotExist, ValueError, TypeError):
            return None

    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        candidate = self.candidate(request)
        if candidate:
            initial = {**candidate.draft_entry(), **initial}
            initial.pop("candidate", None)
        return initial

    def add_view(self, request, form_url="", extra_context=None):
        candidate = self.candidate(request)
        if candidate and request.method == "GET":
            if candidate.entry_id:
                messages.warning(request, "This possible entry is already "
                                 "linked to an entry; saving will link it "
                                 "to the new one instead.")
            messages.info(request, format_html(
                "Adding the possible entry: <em>{}</em>. The fields below "
                "are read from its citation: check them, add what is "
                "missing, and save. Saving marks it added and links it to "
                "this entry{}.", str(candidate),
                "; its author is added if you list none" if
                candidate.author_name() else ""))
        return super().add_view(request, form_url, extra_context)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        candidate = None if change else self.candidate(request)
        if not candidate:
            return
        pub = form.instance
        name = candidate.author_name()
        if name and not pub.authors.exists():
            from .management.commands._loaders import get_reviewer
            Authorship.objects.create(publication=pub,
                                      person=get_reviewer(name), position=1)
        candidate.entry = pub
        candidate.status = Candidate.ADDED
        candidate.save()
        messages.success(request, f"The possible entry “{candidate}” is "
                         "marked added and linked to this entry.")


@admin.register(OpenQuestion)
class OpenQuestionAdmin(admin.ModelAdmin):
    """Questions for the editors, listed on the to-do page."""
    list_display = ("title", "settled", "created")
    list_filter = ("settled",)
    search_fields = ("title", "details")
    autocomplete_fields = ("entries",)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    """Possible entries, listed on the to-do page."""
    list_display = ("author", "citation", "status", "add_it")
    readonly_fields = ("add_it",)
    list_filter = ("status",)
    search_fields = ("author", "citation", "reason")
    autocomplete_fields = ("entry",)

    @admin.display(description="Add it")
    def add_it(self, obj):
        """A link that opens the new-entry form filled in from it."""
        if not obj.pk:
            return "-"
        if obj.entry_id:
            return format_html('<a href="{}">Its entry</a>', reverse(
                "admin:berkeley_publication_change", args=[obj.entry_id]))
        return format_html(
            '<a class="button" href="{}?candidate={}">Add it</a>',
            reverse("admin:berkeley_publication_add"), obj.pk)


@admin.register(IndexTerm)
class IndexTermAdmin(admin.ModelAdmin):
    """The index page's terms, each with the entries that refer to it."""
    list_display = ("name", "entry_count")
    search_fields = ("name",)
    autocomplete_fields = ("entries",)

    @admin.display(description="Entries")
    def entry_count(self, obj):
        return obj.entries.count()


@admin.register(PossibleIndexTerm)
class PossibleIndexTermAdmin(admin.ModelAdmin):
    """Doubts about the index, listed on the to-do page. To settle one,
    add the term or the entries to the index (Index terms) and tick
    "settled"."""
    list_display = ("name", "settled")
    list_filter = ("settled",)
    search_fields = ("name", "details")
    autocomplete_fields = ("entries",)
