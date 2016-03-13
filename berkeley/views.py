import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Person
from .models import Journal
from .models import Publisher
from .models import Publication

from .forms import SearchForm


def search(request):
    form = SearchForm()
    return render(request, 'search.html', {'form': form})


def about(request):
    return render(request, 'about.html', None)


def feedback(request):
    return render(request, 'feedback.html', None)


def detail_view(request, dbkey, cls, html, kwarg_key):
    obj = get_object_or_404(cls, pk=dbkey)
    return render(request, html, {kwarg_key: obj })


def export(request, pub_id):
    return detail_view(request, pub_id, Publication,
            'export.html', 'pub')


def pub_detail(request, pub_id):
    return detail_view(request, pub_id, Publication,
            'pub_detail.html', 'pub')


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
    val = request.GET[get_name]
    if val != '':
        kwargs[kwarg_name] = val


def publications(request):
    kwargs = {}
    add_filter(request, kwargs, 'lname', 'authors__lname')
    add_filter(request, kwargs, 'fname', 'authors__fname')
    add_filter(request, kwargs, 'year_after', 'year__gt')
    add_filter(request, kwargs, 'year_before', 'year__lt')
    add_filter(request, kwargs, 'pub_type', 'pub_type')
    add_filter(request, kwargs, 'subject', 'subject')
    add_filter(request, kwargs, 'journal', 'journal__id')
    add_filter(request, kwargs, 'keyword1', 'keywords__id')
    add_filter(request, kwargs, 'keyword2', 'keywords__id')

    pub_list = Publication.objects.filter(**kwargs).order_by('year')
    for pub in pub_list:
        if pub.pub_type == 'REVW':
            pub.review_of = 'A review of '
    template_data = {'pub_list': pub_list}
    return render(request, 'publications.html', template_data)
