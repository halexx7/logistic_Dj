from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main),
    path("blog/", mainapp.blog),
    path("text/", mainapp.text),
    path("text2/", mainapp.text2),
    path("services/", mainapp.services),
    path("contact/", mainapp.contact),
]
