from os import name

from django.db import models
from django.utils import timezone


class ServicesCategory(models.Model):
    name = models.CharField(verbose_name="name_category", max_length=32, unique=True)
    name_long = models.CharField(verbose_name="name_long", max_length=64)
    desc_category = models.TextField(verbose_name="description")
    is_active = models.BooleanField(verbose_name="category_is_active", default=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="services", max_length=128)
    image = models.ImageField(upload_to="services_images", blank=True)
    description = models.TextField(verbose_name="description", blank=True)
    lifting = models.CharField(verbose_name="lifting", max_length=32)
    price = models.DecimalField(verbose_name="price", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)
    is_active = models.BooleanField(verbose_name="services_activ", default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class News(models.Model):
    title = models.CharField(verbose_name="title_news", max_length=256)
    text = models.TextField(verbose_name="text_news")
    public_date = models.DateTimeField(False, default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.public_date})"


class Benefits(models.Model):
    title = models.CharField(verbose_name="name", max_length=128)
    desc = models.TextField(verbose_name="description", blank=True)


class Team(models.Model):
    full_name = models.CharField(verbose_name="full_name", max_length=256)
    profession = models.CharField(verbose_name="profession", max_length=256)
    photo = models.ImageField(upload_to="team_photo", blank=True)
    email = models.CharField(verbose_name="e-mail", max_length=128)
    phone = models.CharField(verbose_name="phone", max_length=20)


class Contacts(models.Model):
    city = models.CharField(verbose_name="city", max_length=256)
    phone = models.CharField(verbose_name="phone", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=128)
    address = models.CharField(verbose_name="address", max_length=512)
