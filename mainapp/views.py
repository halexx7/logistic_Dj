import datetime
import random

from django.conf import settings
from django.core.cache import cache
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket

from .models import Benefits, Contacts, News, Services, ServicesCategory, Team

def get_links_menu():
    if settings.LOW_CACHE:
        key = "links_menu"
        links_menu = cache.get(key)
        if links_menu is None:
            # print(f'caching {key}')
            links_menu = ServicesCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ServicesCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f"category_{pk}"
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ServicesCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ServicesCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = "services"
        services = cache.get(key)
        if services is None:
            services = Services.objects.filter(is_active=True, category__is_active=True).select_related("category")
            cache.set(key, services)
        return services
    else:
        return Services.objects.filter(is_active=True, category__is_active=True).select_related("category")


def get_product(pk):
    if settings.LOW_CACHE:
        key = f"services_{pk}"
        services = cache.get(key)
        if services is None:
            services = get_object_or_404(Services, pk=pk)
            cache.set(key, services)
        return services
    else:
        return get_object_or_404(Services, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = "products_orederd_by_price"
        products = cache.get(key)
        if products is None:
            products = Services.objects.filter(is_active=True, category__is_active=True).order_by("price")
            cache.set(key, products)
        return products
    else:
        return Services.objects.filter(is_active=True, category__is_active=True).order_by("price")


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f"products_in_category_orederd_by_price_{pk}"
        products = cache.get(key)
        if products is None:
            products = Services.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                "price"
            )
            cache.set(key, products)
        return products
    else:
        return Services.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by("price")


def main(request):
    title = "home"

    caterories = ServicesCategory.objects.all()
    services = get_products()[:4]
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


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_services():
    services = Services.objects.all()
    return random.sample(list(services), 1)[0]


def get_same_services():
    services = get_products()
    same_services = random.sample(list(services), 1)[0]
    same_list = services.exclude(pk=same_services.pk)[:3]
    return (same_services, same_list)


def get_popular_goods(services):
    popular_services = Services.objects.all().exclude(pk=services.pk)
    return random.sample(list(popular_services), 3)


def services(request, pk=None, page=1):
    title = "services"
    links_menu = get_links_menu()
    basket = get_basket(request.user)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == "0":
            category = {"pk": 0, "name": "All"}
            services = get_products_orederd_by_price()
        else:
            category = get_category(pk)
            services = get_products_orederd_by_price()

        paginator = Paginator(services, 2)
        try:
            services_paginator = paginator.page(page)
        except PageNotAnInteger:
            services_paginator = paginator.page(1)
        except EmptyPage:
            services_paginator = paginator.page(paginator.num_pages)
        content = {
            "title": title,
            "services": services_paginator,
            "category": category,
            "links_menu": links_menu,
            "media_url": settings.MEDIA_URL,
        }
        return render(request, "mainapp/services_list.html", content)
    hot_services = get_hot_services()
    content = {
        "title": title,
        "links_menu": links_menu,
        "media_url": settings.MEDIA_URL,
        "popular": get_popular_goods(hot_services),
        "hot": hot_services,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/services.html", content)


def service(request, pk):
    title = "service"

    service = get_object_or_404(Services, pk=pk)
    content = {
        "title": title,
        "links_menu": ServicesCategory.objects.all(),
        "service": service,
        "popular": get_popular_goods(service),
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/service.html", content)


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
