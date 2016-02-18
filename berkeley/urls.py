from django.conf.urls import url

from . import views

app_name = 'berkeley'


urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^about/*$', views.about, name='about'),
    url(r'^feedback/*$', views.feedback, name='feedback'),
    url(r'^publications/*$', views.publications, name='publications'),
    url(r'^pub_detail/(?P<pub_id>[0-9]+)/$', 
        views.pub_detail, name='pub_detail'),
    url(r'^person_detail/(?P<person_id>[0-9]+)/$', 
        views.person_detail, name='person_detail'),
    url(r'^journal_detail/(?P<journal_id>[0-9]+)/$', 
        views.journal_detail, name='journal_detail'),
    url(r'^publisher_detail/(?P<publisher_id>[0-9]+)/$', 
        views.publisher_detail, name='publisher_detail'),
]
