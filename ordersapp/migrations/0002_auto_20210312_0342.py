# Generated by Django 2.2.17 on 2021-03-12 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ordersapp", "0001_orders"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="product",
            new_name="service",
        ),
    ]
