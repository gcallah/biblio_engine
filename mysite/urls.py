"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.urls import include, re_path
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^oakeshott/', include('berkeley.urls')),
    # old URLs: send /berkeley/... to /oakeshott/...
    re_path(r'^berkeley/(?P<rest>.*)$',
            RedirectView.as_view(url='/oakeshott/%(rest)s',
                                 permanent=True, query_string=True)),
    re_path(r'^admin/', admin.site.urls),
]
