import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Person
from .models import Publication


def index(request):
    return render(request, 'berkeley/index.html', None)

# 
# def author_detail(request, person_id):
#     author = get_object_or_404(Author, pk=author_id)
#     pub_list = None
#     pub_list = Publication.objects.filter(author=author_id)
#     return render(request, 'berkeley/author_detail.html',
#             {'author': person, 'pub_list': pub_list, 'role':
#                 person.get_role_display()})
# 

def publications(request):
    lname = request.GET['lname']
    person_list = get_list_or_404(Person, lname=lname)
    pub_list = []
#    for person in person_list:
#        logging.debug("Fetching pubs for %s %s" % (person.fname, person.lname))
#        pubs = Publication.objects.filter(prim_author.lname=person.lname)
#        pub_list.append(pubs)
    pub_list = Publication.objects.all()  # a temporary kludge 

    return render(request, 'berkeley/publications.html',  {'lname': lname,
        'pub_list': pub_list})
