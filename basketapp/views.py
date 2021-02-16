from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from basketapp.models import Basket
from mainapp.models import Services


def basket(request):
    # content = {}
    # return render(request, "basketapp/basket.html", content)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_add(request, pk):
    service = get_object_or_404(Services, pk=pk)
    basket = Basket.objects.filter(user=request.user, service=service).first()

    if not basket:
        basket = Basket(user=request.user, service=service)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_remove(request):
    # content = {}
    # return render(request, "basketapp/basket.html", content)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))