# Generated by Django 4.2 on 2023-07-06 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0018_alter_rating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkitem',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='produkitem',
            name='ratings',
        ),
    ]
