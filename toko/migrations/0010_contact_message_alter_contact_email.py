# Generated by Django 4.2 on 2023-07-04 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0009_contact_alter_produkitem_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]