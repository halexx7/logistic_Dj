# Generated by Django 2.2.17 on 2021-02-26 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_servicescategory_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='services_activ'),
        ),
    ]
