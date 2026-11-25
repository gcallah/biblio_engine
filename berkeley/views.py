import logging
logger = logging.getLogger(__name__)

from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.urls import reverse

from .models import AdminEmail
from .models import Candidate
from .models import OpenQuestion
from .models import IndexTerm
from .models import PossibleIndexTerm
from .models import Journal
from .models import Person
from .models import Publisher
from .models import Publication
from .models import REVIEW_TYPES
from .models import Site

from .forms import EditorLoginForm, SearchForm
from . import duplicates as dups
from .models import NotDuplicate

# editors are staff accounts (manage.py add_editor); anyone else is sent
# to the login page, as login_required would
editor_required = user_passes_test(lambda u: u.is_active and u.is_staff)


def get_hdr():
    site_hdr = "Bibliography Search"
    site_list = Site.objects.all()
    for site in site_list:
        site_hdr = site.header
        break   # since we only expect a single site record!
    return site_hdr


def search(request):
    site_hdr = get_hdr()
    form = SearchForm()
    return render(request, 'search.html', {'form': form, 'header': site_hdr})


def about(request):
    site_hdr = get_hdr()
    return render(request, 'about.html', {'header': site_hdr})


def feedback(request):
    site_hdr = get_hdr()
    email_list = AdminEmail.objects.all()
    comma_del_emails = ""
    for email in email_list:
        comma_del_emails = comma_del_emails + email.email_addr + ","
    comma_del_emails = comma_del_emails[:-1]
    return render(request, 'feedback.html', {'emails': comma_del_emails,
        'header': site_hdr})


def detail_view(request, dbkey, cls, html, kwarg_key):
    site_hdr = get_hdr()
    obj = get_object_or_404(cls, pk=dbkey)
    return render(request, html, {kwarg_key: obj, 'header': site_hdr })


def export(request, pub_id):
    return detail_view(request, pub_id, Publication,
            'export.html', 'pub')


def export_citations(request, pub_id):
    """The citation rows alone, loaded into the results-table popup."""
    pub = get_object_or_404(Publication, pk=pub_id)
    return render(request, 'export_citations.html', {'pub': pub})


def pub_detail(request, pub_id):
    return detail_view(request, pub_id, Publication,
            'pub_detail.html', 'pub')


@editor_required
def edit_pub(request, pub_id):
    """Editing is done in the Django admin: send the editor to the
    entry's admin page."""
    pub = get_object_or_404(Publication, pk=pub_id)
    return redirect(reverse('admin:berkeley_publication_change',
                            args=[pub.id]))


@editor_required
def todo(request):
    """The editors' to-do page: open questions about existing entries,
    then the possible entries still to decide on. Both are kept up to date
    in the admin."""
    questions = (OpenQuestion.objects.filter(settled=False)
                 .prefetch_related('entries'))
    candidates = Candidate.objects.filter(
        status__in=(Candidate.UNDECIDED, Candidate.NOT_CHECKED))
    groups = [(label, [c for c in candidates if c.status == status])
              for status, label in Candidate.STATUS_CHOICES
              if status in (Candidate.UNDECIDED, Candidate.NOT_CHECKED)]
    index_doubts = (PossibleIndexTerm.objects.filter(settled=False)
                    .prefetch_related('entries__authorship_set__person',
                                      'entries__pub_reviewed'))
    in_index = set(IndexTerm.objects.filter(
        name__in=[d.name for d in index_doubts]).values_list('name',
                                                              flat=True))
    for doubt in index_doubts:
        doubt.in_index = doubt.name in in_index
    found = []
    for kind, label, pairs in dups.possible_duplicates():
        rows = []
        for a, b in pairs:
            rows.append({'sides': [
                dict(zip(('name', 'url', 'note'), dups.describe(obj)),
                     obj=obj, other=other)
                for obj, other in ((a, b), (b, a))]})
        found.append((kind, label, rows))
    return render(request, 'todo.html', {
        'header': get_hdr(), 'questions': questions, 'groups': groups,
        'index_doubts': index_doubts, 'duplicates': found,
        'decided': Candidate.objects.count() - len(candidates)})


def _todo_duplicates():
    return redirect(reverse('berkeley:todo') + '#duplicates')


@editor_required
@require_POST
def merge(request, kind, keep_id, drop_id):
    """"Keep this one" on the to-do page: merge the other record of a
    possible duplicate into this one."""
    model = dups.KINDS.get(kind)
    if not model:
        return _todo_duplicates()
    keep = get_object_or_404(model, pk=keep_id)
    drop = get_object_or_404(model, pk=drop_id)
    dropped = str(drop)
    try:
        dups.merge(keep, drop)
    except (ValueError, RuntimeError) as err:
        messages.error(request, f"Not merged: {err}")
    else:
        logger.info("%s merged %s %s into %s", request.user, kind,
                    drop_id, keep_id)
        messages.success(request, f"Merged “{dropped}” into “{keep}”.")
    return _todo_duplicates()


@editor_required
@require_POST
def not_duplicates(request, kind, first_id, second_id):
    """"Not the same": take a pair off the possible duplicates."""
    if kind in dups.KINDS:
        first, second = sorted((int(first_id), int(second_id)))
        NotDuplicate.objects.get_or_create(kind=kind, first_id=first,
                                           second_id=second)
    return _todo_duplicates()


def index(request):
    """The index: every significant term, A to Z, each with links to
    the entries that refer to it."""
    terms = IndexTerm.objects.prefetch_related(
        'entries__authorship_set__person', 'entries__pub_reviewed')
    letters = {}
    for term in terms:
        term.ordered_entries = sorted(
            term.entries.all(), key=lambda p: (p.year, str(p).lower()))
        first = term.name[:1].upper()
        letters.setdefault(first if first.isalpha() else '#', []).append(term)
    return render(request, 'index.html', {
        'header': get_hdr(), 'letters': sorted(letters.items())})


class LoginView(auth_views.LoginView):
    """The editors' login page, in the site's own style. There is no
    sign-up: logins are made by an administrator (manage.py add_editor)."""
    template_name = 'login.html'
    authentication_form = EditorLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = get_hdr()
        return context


def person_detail(request, person_id):
    return detail_view(request, person_id, Person,
            'person_detail.html', 'person')


def journal_detail(request, journal_id):
    return detail_view(request, journal_id, Journal,
            'journal_detail.html', 'journal')


def publisher_detail(request, publisher_id):
    return detail_view(request, publisher_id, Publisher,
            'publisher_detail.html', 'publisher')


def add_filter(request, kwargs, get_name, kwarg_name):
    val = request.GET.get(get_name, '').strip()
    if val:
        kwargs[kwarg_name] = val


def add_year_filter(request, kwargs, get_name, kwarg_name):
    val = request.GET.get(get_name, '').strip()
    if val.isdigit():
        kwargs[kwarg_name] = int(val)


def publications(request):
    site_hdr = get_hdr()
    kwargs = {}
    add_filter(request, kwargs, 'lname', 'authors__lname__icontains')
    add_filter(request, kwargs, 'reviewed', 'reviewees__lname__icontains')
    add_filter(request, kwargs, 'pub_type', 'pub_type')
    add_year_filter(request, kwargs, 'start_year', 'year__gte')
    add_year_filter(request, kwargs, 'end_year', 'year__lte')
    add_filter(request, kwargs, 'subject', 'subject')
    add_filter(request, kwargs, 'keyword1', 'keywords__id')

    pub_list = (Publication.objects.filter(**kwargs).distinct()
                .order_by('year')
                .select_related('journal__publisher', 'publisher', 'collection',
                                'subject')
                .select_related('pub_reviewed')
                .prefetch_related('authorship_set__person',
                                  'editorship_set__person'))
    for pub in pub_list:
        if pub.pub_type in REVIEW_TYPES:
            pub.review_of = pub.review_title()
    template_data = {'pub_list': pub_list, 'header': site_hdr}
    return render(request, 'publications.html', template_data)
