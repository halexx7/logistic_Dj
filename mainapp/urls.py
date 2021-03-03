from django.urls import re_path

import mainapp.views as mainapp

from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    re_path(r"^$", mainapp.services, name="index"),
    re_path(r"^category/(?P<pk>\d+)/$", mainapp.services, name="category"),
    re_path(r"^category/(?P<pk>\d+)/page/(?P<page>\d+)/$", mainapp.services, name="page"),
    re_path(r"^service/(?P<pk>\d+)/$", mainapp.service, name="service"),
]
