import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Person
from .models import Journal
from .models import Publisher
from .models import Publication


def index(request):
    return render(request, 'index.html', None)


def about(request):
    return render(request, 'about.html', None)


def pub_detail(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    return render(request, 'pub_detail.html',
            {'pub': pub })


def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'person_detail.html',
            {'person': person })


def journal_detail(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    return render(request, 'journal_detail.html',
            {'journal': journal })


def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'publisher_detail.html',
            {'publisher': publisher })


def publications(request):
    kwargs = {}
    lname = request.GET['lname']
    if lname != '':
        kwargs['authors__lname'] = lname
    fname = request.GET['fname']
    if fname != '':
        kwargs['authors__fname'] = fname
    year = request.GET['year']
    if year != '':
        kwargs['year'] = year
    pub_list = Publication.objects.filter(**kwargs).order_by('year')
    template_data = {'lname': lname, 'pub_list': pub_list}
    return render(request, 'publications.html', template_data)
