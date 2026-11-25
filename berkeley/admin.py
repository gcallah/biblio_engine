"""The Django admin, which is where logged-in editors edit the
bibliography: the edit pencils on the site link to these pages. Logins are
made with manage.py add_editor; every editor can edit everything."""
from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.db.models import Q
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
from .models import NotDuplicate
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
# pairs marked "Not the same" on the to-do page; delete one to list it again
admin.site.register(NotDuplicate)
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
    # only on "Add it" (a new entry from a possible entry): an author or
    # publisher named in its citation but not yet in the database, made
    # when the entry is saved (see PublicationAdmin)
    new_author = forms.CharField(
        label="Author to add", required=False,
        help_text="From the citation, and not yet in the bibliography: "
        "saving adds this person (last name, initials) as the author, "
        "unless you choose authors below. Clear it to add no one.")
    # on "Add it", when the citation's author is already in the
    # bibliography: who that is, at the top of the form, since the
    # Authors list where they are chosen is at its foot
    found_author = forms.CharField(
        label="Author", required=False, disabled=True,
        help_text="From the citation, and already in the bibliography: "
        "chosen for you under Authors, at the foot of the form. There is "
        "no need to add them again.")
    new_publisher = forms.CharField(
        label="Publisher to add", required=False,
        help_text="From the citation, and not yet in the bibliography: "
        "saving adds this publisher (Place: Name) unless you choose one "
        "above. Clear it to add none.")

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
            person = self.known_author(candidate)
            if person:
                initial["found_author"] = str(person)
            elif candidate.author_name():
                initial["new_author"] = candidate.author
        return initial

    @staticmethod
    def known_author(candidate):
        """The person in the database the possible entry's author is,
        if any."""
        from .management.commands._loaders import find_person
        name = candidate.author_name()
        return find_person(name) if name else None

    def get_fields(self, request, obj=None):
        """The author and new-publisher boxes only on "Add it"."""
        extra = ("found_author", "new_author", "new_publisher")
        fields = [f for f in super().get_fields(request, obj)
                  if f not in extra]
        candidate = None if obj else self.candidate(request)
        if not candidate:
            return fields
        # each next to what it stands in for (authors are an inline, at
        # the foot of the form, so the author box goes first)
        fields.insert(fields.index("publisher") + 1, "new_publisher")
        author = ("found_author" if self.known_author(candidate)
                  else "new_author")
        return [author, *fields]

    def get_formset_kwargs(self, request, obj, inline, prefix):
        """On "Add it", the authors list starts with the citation's
        author when that person is already in the database."""
        kwargs = super().get_formset_kwargs(request, obj, inline, prefix)
        candidate = None if obj.pk else self.candidate(request)
        if (candidate and request.method == "GET"
                and isinstance(inline, AuthorshipInline)):
            person = self.known_author(candidate)
            if person:
                kwargs["initial"] = [{"person": person.id, "position": 1}]
        return kwargs

    def save_model(self, request, obj, form, change):
        """A publisher typed into "Publisher to add" (Place: Name) is made
        when no publisher is chosen."""
        from .management.commands._loaders import (find_publisher,
                                                   get_publisher)
        text = form.cleaned_data.get("new_publisher", "").strip()
        if text and not obj.publisher_id:
            place, _, name = text.rpartition(":")
            # "Belmont, CA": the city, then its state or province
            city, _, province = (p.strip() for p in place.partition(","))
            name = name.strip()
            obj.publisher = (find_publisher(name, city) or get_publisher(
                name, {}, city=city or None, province=province or None))
        super().save_model(request, obj, form, change)

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
                "this entry.", str(candidate)))
        return super().add_view(request, form_url, extra_context)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        candidate = None if change else self.candidate(request)
        if not candidate:
            return
        pub = form.instance
        text = form.cleaned_data.get("new_author", "").strip()
        name = Candidate(author=text).author_name() if text else None
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


def entry_label(pub):
    """'Title (Surname, Surname, 1962)', as on the index page."""
    names = [a.lname for a in pub.ordered_authors()] + [str(pub.year)]
    return f"{pub} ({', '.join(names)})"


class IndexTermForm(forms.ModelForm):
    """An index term's entries as tick boxes: the entries under it, and
    those a possible index term of the same name (on the to-do page)
    suggests. Saving keeps the ticked ones under the term."""
    entries = forms.ModelMultipleChoiceField(
        queryset=Publication.objects.none(), required=False,
        widget=forms.CheckboxSelectMultiple, label="Entries",
        help_text="Tick each entry that belongs under this term, and "
        "untick any that does not; the index lists the ticked ones. "
        "Those marked “Possible” are suggested on the to-do page and not "
        "under the term yet.")
    more_entries = forms.ModelMultipleChoiceField(
        queryset=Publication.objects.all(), required=False,
        widget=AutocompleteSelectMultiple(
            IndexTerm._meta.get_field("entries"), admin.site),
        label="Other entries to add",
        help_text="For an entry not in the list above: type part of its "
        "title, choose it, and save.")
    settle = forms.BooleanField(
        required=False, initial=True, label="Settled",
        help_text="Take this term off the to-do page's possible index "
        "terms when saved.")

    class Meta:
        model = IndexTerm
        fields = ("name", "entries")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from django.db.models import Exists, OuterRef
        name = (self.data.get("name") or self.initial.get("name")
                or self.instance.name or "")
        self.doubts = PossibleIndexTerm.objects.filter(name=name,
                                                       settled=False)
        links = IndexTerm.entries.through.objects.filter(
            indexterm_id=self.instance.pk, publication=OuterRef("pk"))
        wanted = Q(possible_index_terms__in=self.doubts)
        if self.instance.pk:
            wanted |= Q(index_terms=self.instance.pk)
        choices = (Publication.objects.filter(wanted)
            .distinct().annotate(under=Exists(links))
            .order_by("under", "year", "title")
            .prefetch_related("authorship_set__person"))
        field = self.fields["entries"]
        field.queryset = choices
        field.label_from_instance = lambda pub: (
            entry_label(pub) if pub.under
            else f"Possible: {entry_label(pub)}")
        if "settle" in self.fields and not self.doubts:
            del self.fields["settle"]


@admin.register(IndexTerm)
class IndexTermAdmin(admin.ModelAdmin):
    """The index page's terms, each with the entries that refer to it,
    chosen with tick boxes (IndexTermForm)."""
    form = IndexTermForm
    list_display = ("name", "entry_count")
    search_fields = ("name",)

    def get_fields(self, request, obj=None):
        name = obj.name if obj else (request.POST.get("name")
                                     or request.GET.get("name"))
        settle = ["settle"] if PossibleIndexTerm.objects.filter(
            name=name or "", settled=False).exists() else []
        return ["name", "entries", "more_entries", *settle]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        term = form.instance
        term.entries.add(*form.cleaned_data.get("more_entries", []))
        if form.cleaned_data.get("settle"):
            form.doubts.update(settled=True)

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
