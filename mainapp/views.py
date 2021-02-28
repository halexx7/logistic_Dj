import datetime
import random

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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


def get_popular_goods(services):
    popular_services = Services.objects.all().exclude(pk=services.pk)
    return random.sample(list(popular_services), 3)


def services(request, pk=None, page=1):
    title = "services"
    links_menu = ServicesCategory.objects.all()
    basket = get_basket(request.user)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "All"}
            services = Services.objects.filter(is_active=True, category__is_active=True).order_by("price")
        else:
            category = get_object_or_404(ServicesCategory, pk=pk)
            services = Services.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                "price"
            )

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
            "basket": basket,
        }
        return render(request, "mainapp/services_list.html", content)
    hot_services = get_hot_services()
    content = {
        "title": title,
        "links_menu": links_menu,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        "popular": get_popular_goods(hot_services),
        "hot": hot_services,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/services.html", content)

def products(request, pk=None, page=1):
   

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                "price"
            )

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products_paginator,
            "media_url": settings.MEDIA_URL,
            "basket": basket,
        }
        return render(request, "mainapp/products_list.html", content)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        "hot_product": hot_product,
    }
    return render(request, "mainapp/products.html", content)


def service(request, pk):
    title = "service"

    service = get_object_or_404(Services, pk=pk)
    content = {
        "title": title,
        "links_menu": ServicesCategory.objects.all(),
        "service": service,
        "basket": get_basket(request.user),
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
