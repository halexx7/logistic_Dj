# Generated by Django 2.2.17 on 2021-02-23 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_fill_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicescategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='category_is_active'),
        ),
    ]
