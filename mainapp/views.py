from django.conf import settings
from django.shortcuts import render
import datetime

from .models import Services, ServicesCategory, News, Benefits, Team, Contacts


def main(request):
    title = "home"

    caterories = ServicesCategory.objects.all()
    services = Services.objects.all()
    news = News.objects.all()
    benefits_list = Benefits.objects.all()
    team = Team.objects.all()

    content = {
        "title": title,
        "caterories": caterories,
        "services": services,
        "benefits_list": benefits_list,
        "team": team,
        "news": news,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/index.html", content)


def blog(request):
    title = "blog"

    news = News.objects.all()

    content = {
        "title": title,
        "news": news,
    }
    return render(request, "mainapp/blog.html", content)


def text(request):
    title = "Privacy Policy"
    content = {"title": title}
    return render(request, "mainapp/text.html", content)


def text2(request):
    title = "Terms & Conditions"
    content = {"title": title}
    return render(request, "mainapp/text-2.html", content)


def services(request, pk=None):
    title = "services"
    services = Services.objects.all()
    links_menu = ServicesCategory.objects.all()

    content = {
        "title": title,
        "services": services,
        "links_menu": links_menu,
        "media_url": settings.MEDIA_URL,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/services.html", content)


def contact(request):
    title = "contacts"
    visit_date = datetime.datetime.now()
    contacts = Contacts.objects.all()
    content = {
        "title": title,
        "visit_date": visit_date,
        "contacts": contacts,
    }
    return render(request, "mainapp/contact.html", content)
