# Generated by Django 3.2.6 on 2021-10-25 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20211025_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='order',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='product',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='quantity',
        ),
    ]