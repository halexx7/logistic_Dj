from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Services


@login_required
def basket(request):
    title = "basket"
    basket_items = Basket.objects.filter(user=request.user).order_by("service__category")
    content = {"title": title, "basket_items": basket_items, "media_url": settings.MEDIA_URL}
    return render(request, "basketapp/basket.html", content)


@login_required
def basket_add(request, pk):
    if "login" in request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(reverse("services:service", args=[pk]))
    service = get_object_or_404(Services, pk=pk)
    basket = Basket.objects.filter(user=request.user, service=service).first()

    if not basket:
        basket = Basket(user=request.user, service=service)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        print(f"{pk} - {quantity}")
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by("service__category")

        content = {"basket_items": basket_items, "media_url": settings.MEDIA_URL}

        result = render_to_string("basketapp/includes/inc_basket_list.html", content)

        return JsonResponse({"result": result})