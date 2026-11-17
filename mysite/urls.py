"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
import re

from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from django.views.generic import RedirectView

PREFIX = re.escape(settings.BIBLIO_URL_PREFIX)

urlpatterns = [
    # bare site root: send visitors to the bibliography's search page
    re_path(r'^$', RedirectView.as_view(pattern_name='berkeley:search',
                                        permanent=False)),
    re_path(rf'^{PREFIX}/', include('berkeley.urls')),
    re_path(r'^admin/', admin.site.urls),
]

# old URLs: send e.g. /berkeley/... to /oakeshott/...
for old in settings.BIBLIO_OLD_URL_PREFIXES:
    urlpatterns.append(
        re_path(rf'^{re.escape(old)}/(?P<rest>.*)$',
                RedirectView.as_view(
                    url=f'/{settings.BIBLIO_URL_PREFIX}/%(rest)s',
                    permanent=True, query_string=True)))
