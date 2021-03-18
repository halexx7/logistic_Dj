from django.conf import settings
from django.db import models
from django.shortcuts import get_object_or_404

from mainapp.models import Services


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)
    add_datetime = models.DateTimeField(verbose_name="create_date", auto_now_add=True)

    @property
    def service_cost(self):
        "return cost of all products this type"
        return self.service.price * self.quantity

    @property
    def total_quantity(self):
        "return total quantity for user"
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        "return total cost for user"
        _items = Basket.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.service_cost, _items)))
        return _totalcost

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by("service__category")

    @staticmethod
    def get_item(pk):
        return get_object_or_404(Basket, pk=pk)
