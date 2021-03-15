from django.conf import settings
from django.db import models
from django.shortcuts import get_object_or_404

from mainapp.models import Services


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.service.quantity += object.quantity
            object.service.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)
    add_datetime = models.DateTimeField(verbose_name="create_date", auto_now_add=True)

    objects = BasketQuerySet.as_manager()

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

    # Object's saving method
    def save(self, *args, **kwargs):
        if self.pk:
            self.service.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.service.quantity -= self.quantity
        self.service.save()
        super(self.__class__, self).save(*args, **kwargs)

    # Object's deleting method
    def delete(self):
        self.service.quantity += self.quantity
        self.service.save()
        super(self.__class__, self).delete()
