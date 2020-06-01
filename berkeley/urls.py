from django.urls import re_path

from . import views

app_name = 'berkeley'


urlpatterns = [
    re_path(r'^$', views.search, name='search'),
    re_path(r'^about/*$', views.about, name='about'),
    re_path(r'^feedback/*$', views.feedback, name='feedback'),
    re_path(r'^publications/*$', views.publications, name='publications'),
    re_path(r'^export/(?P<pub_id>[0-9]+)/$', views.export, name='export'),
    re_path(r'^pub_detail/(?P<pub_id>[0-9]+)/$', 
            views.pub_detail, name='pub_detail'),
    re_path(r'^edit_pub/(?P<pub_id>[0-9]+)/$', 
            views.edit_pub, name='edit_pub'),
    re_path(r'^person_detail/(?P<person_id>[0-9]+)/$', 
            views.person_detail, name='person_detail'),
    re_path(r'^journal_detail/(?P<journal_id>[0-9]+)/$', 
            views.journal_detail, name='journal_detail'),
    re_path(r'^publisher_detail/(?P<publisher_id>[0-9]+)/$', 
            views.publisher_detail, name='publisher_detail'),
]
