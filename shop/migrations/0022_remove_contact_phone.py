# Generated by Django 3.2.6 on 2021-10-25 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20211025_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
