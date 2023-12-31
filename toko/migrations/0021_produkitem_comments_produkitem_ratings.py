# Generated by Django 4.2 on 2023-07-06 09:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toko', '0020_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkitem',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='commented_products', through='toko.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='produkitem',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='rated_products', through='toko.Rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
