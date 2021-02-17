from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.services, name="index"),
    path("category/<int:pk>/", mainapp.services, name="category"),
    path("service/<int:pk>/", mainapp.service, name="service"),
]
