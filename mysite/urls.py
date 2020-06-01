"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^berkeley/', include('berkeley.urls')),
    re_path(r'^admin/', admin.site.urls),
]
