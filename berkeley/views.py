import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import AdminEmail
from .models import Journal
from .models import Person
from .models import Publisher
from .models import Publication
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


def pub_detail(request, pub_id):
    return detail_view(request, pub_id, Publication,
            'pub_detail.html', 'pub')


def edit_pub(request, pub_id):
    return detail_view(request, pub_id, Publication,
            'edit_pub.html', 'pub')


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
    #val = request.GET.get[get_name]
    val = request.GET.get(get_name)
    if val != '':
        kwargs[kwarg_name] = val


def publications(request):
    site_hdr = get_hdr()
    kwargs = {}
    add_filter(request, kwargs, 'lname', 'authors__lname')
    add_filter(request, kwargs, 'pub_type', 'pub_type')
    add_filter(request, kwargs, 'subject', 'subject')
    add_filter(request, kwargs, 'keyword2', 'keywords__id')

    pub_list = Publication.objects.filter(**kwargs).order_by('year')
    for pub in pub_list:
        if pub.pub_type == 'REVW':
            pub.review_of = 'A review of '
    template_data = {'pub_list': pub_list, 'header': site_hdr}
    return render(request, 'publications.html', template_data)
