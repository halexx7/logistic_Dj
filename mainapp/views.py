import datetime
import random

from django.conf import settings
from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket

from .models import Benefits, Contacts, News, Services, ServicesCategory, Team


def main(request):
    title = "home"

    caterories = ServicesCategory.objects.all()
    services = Services.objects.all()[:4]
    news = News.objects.all()
    benefits_list = Benefits.objects.all()
    team = Team.objects.all()
    basket = get_basket(request.user)

    content = {
        "title": title,
        "caterories": caterories,
        "services": services,
        "benefits_list": benefits_list,
        "team": team,
        "news": news,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
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


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_services():
    services = Services.objects.all()
    return random.sample(list(services), 1)[0]


def get_same_services(hot_services):
    same_services = Services.objects.filter(category=hot_services.category).exclude(pk=hot_services.pk)[:3]
    return same_services


def services(request, pk=None):
    title = "services"
    links_menu = ServicesCategory.objects.all()
    basket = get_basket(request.user)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        # or you can use this
        # _basket = request.user.basket.all()
        # print(f'basket / _basket: {len(_basket)} / {len(basket)}')

    if pk is not None:
        if pk == 0:
            services = Services.objects.all().order_by("price")
            category = {"name": "All"}
        else:
            category = get_object_or_404(ServicesCategory, pk=pk)
            services = Services.objects.filter(category__pk=pk).order_by("price")
        content = {
            "title": title,
            "services": services,
            "category": category,
            "links_menu": links_menu,
            "media_url": settings.MEDIA_URL,
            "basket": basket,
        }
        return render(request, "mainapp/services_list.html", content)
    hot_services = get_hot_services()
    same_services = get_same_services(hot_services)
    content = {
        "title": title,
        "links_menu": links_menu,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        "same_services": same_services,
        "hot_services": hot_services,
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
