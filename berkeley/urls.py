from django.conf.urls import url

from . import views

app_name = 'berkeley'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^publications/*$', views.publications, name='publications'),
    url(r'^pub_detail/(?P<pub_id>[0-9]+)/$', 
        views.pub_detail, name='pub_detail'),
    url(r'^person_detail/(?P<person_id>[0-9]+)/$', 
        views.person_detail, name='person_detail'),
]
