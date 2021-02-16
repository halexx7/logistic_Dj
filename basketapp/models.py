from django.conf import settings
from django.db import models

from mainapp.models import Services


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)
    add_datetime = models.DateTimeField(verbose_name="время добавления", auto_now_add=True)