from django.contrib import admin

from .models import Services, ServicesCategory, News, Benefits, Team, Contacts

admin.site.register(ServicesCategory)
admin.site.register(Services)
admin.site.register(News)
admin.site.register(Benefits)
admin.site.register(Team)
admin.site.register(Contacts)