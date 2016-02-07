import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Person
from .models import Publication


def index(request):
    return render(request, 'berkeley/index.html', None)


def pub_detail(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    return render(request, 'berkeley/pub_detail.html',
            {'pub': pub })


def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'berkeley/person_detail.html',
            {'person': person })


def publications(request):
    lname = request.GET['lname']
    pub_list = Publication.objects.filter(
        authors__lname=lname 
    )
    template_data = {'lname': lname, 'pub_list': pub_list}
    return render(request, 'berkeley/publications.html', template_data)
