from django.conf import settings
from django.conf.urls.static import static
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
    path("services/railway", mainapp.services, name='services_railway'),
    path("services/water", mainapp.services, name='services_water'),
    path("services/air", mainapp.services, name='services_air'),
    path("contact/", mainapp.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
