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


def detail_view(request, dbkey, cls, html, kwarg_key):
    obj = get_object_or_404(cls, pk=dbkey)
    return render(request, html, {kwarg_key: obj })


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


def publications(request):
    kwargs = {}
    lname = request.GET['lname']
    if lname != '':
        kwargs['authors__lname'] = lname
    fname = request.GET['fname']
    if fname != '':
        kwargs['authors__fname'] = fname
    year_after = request.GET['year_after']
    if year_after != '':
        kwargs['year__gt'] = year_after
    year_before = request.GET['year_before']
    if year_before != '':
        kwargs['year__lt'] = year_before
    subject = request.GET['subject']
    if subject != '':
        kwargs['subject'] = subject
    keyword_id = request.GET['keyword']
    if keyword_id != '':
        kwargs['keywords__id'] = keyword_id

    pub_list = Publication.objects.filter(**kwargs).order_by('year')
    template_data = {'lname': lname, 'pub_list': pub_list}
    return render(request, 'publications.html', template_data)
