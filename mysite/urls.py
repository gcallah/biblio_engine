"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.urls import include, re_path
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    # bare site root: send visitors to the bibliography's search page
    re_path(r'^$', RedirectView.as_view(pattern_name='berkeley:search',
                                        permanent=False)),
    re_path(r'^oakeshott/', include('berkeley.urls')),
    # old URLs: send /berkeley/... to /oakeshott/...
    re_path(r'^berkeley/(?P<rest>.*)$',
            RedirectView.as_view(url='/oakeshott/%(rest)s',
                                 permanent=True, query_string=True)),
    re_path(r'^admin/', admin.site.urls),
]
