from django.conf.urls import url

from . import views

app_name = 'berkeley'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^publications/*$', views.publications, name='publications'),
#    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_detail, name='author_detail'),
]
