# Generated by Django 4.2 on 2023-07-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0014_rating_comment_produkitem_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]