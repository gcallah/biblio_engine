import logging
logger = logging.getLogger(__name__)

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.urls import reverse

from .models import AdminEmail
from .models import Candidate
from .models import OpenQuestion
from .models import Journal
from .models import Person
from .models import Publisher
from .models import Publication
from .models import REVIEW_TYPES
from .models import Site

from .forms import SearchForm


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


@login_required
def edit_pub(request, pub_id):
    """Editing is done in the Django admin: send the editor to the
    entry's admin page."""
    pub = get_object_or_404(Publication, pk=pub_id)
    return redirect(reverse('admin:berkeley_publication_change',
                            args=[pub.id]))


@login_required
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
    return render(request, 'todo.html', {
        'header': get_hdr(), 'questions': questions, 'groups': groups,
        'decided': Candidate.objects.count() - len(candidates)})


class LoginView(auth_views.LoginView):
    """The editors' login page, in the site's own style. There is no
    sign-up: logins are made by an administrator (manage.py add_editor)."""
    template_name = 'login.html'

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
