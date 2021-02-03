from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main, name='main'),
    path("blog/", mainapp.blog, name='blog'),
    path("text/", mainapp.text, name='text'),
    path("text2/", mainapp.text2, name='text2'),
    path("services/", mainapp.services, name='services'),
    path("contact/", mainapp.contact, name='contact'),
]
